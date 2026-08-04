import hashlib
import sqlite3
from pathlib import Path

import chromadb

from config import CHROMA_DIR, SAMPLE_REPO, SCHEMA_FILE, SQLITE_DB, STORAGE_DIR
from symbol_extractor import extract_python_symbols


def hash_text(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def chunk_lines(text, chunk_size=30):
    lines = text.splitlines()
    for index in range(0, len(lines), chunk_size):
        start = index + 1
        end = min(index + chunk_size, len(lines))
        yield start, end, "\n".join(lines[index:end])


def setup_sqlite():
    STORAGE_DIR.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(SQLITE_DB)
    connection.executescript(SCHEMA_FILE.read_text())
    return connection


def index_file(connection, collection, path):
    text = path.read_text()
    relative_path = str(path.relative_to(SAMPLE_REPO))
    line_count = len(text.splitlines())

    connection.execute(
        """
        INSERT OR REPLACE INTO files(path, language, content_hash, line_count)
        VALUES (?, ?, ?, ?)
        """,
        (relative_path, "python", hash_text(text), line_count),
    )

    file_id = connection.execute(
        "SELECT id FROM files WHERE path = ?",
        (relative_path,),
    ).fetchone()[0]

    connection.execute("DELETE FROM symbols WHERE file_id = ?", (file_id,))
    old_chunks = connection.execute(
        "SELECT id FROM chunks WHERE file_id = ?",
        (file_id,),
    ).fetchall()
    for (chunk_id,) in old_chunks:
        connection.execute("DELETE FROM chunks_fts WHERE chunk_id = ?", (chunk_id,))
    connection.execute("DELETE FROM chunks WHERE file_id = ?", (file_id,))

    for symbol in extract_python_symbols(text):
        connection.execute(
            """
            INSERT INTO symbols(file_id, name, symbol_type, start_line, end_line)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                file_id,
                symbol["name"],
                symbol["symbol_type"],
                symbol["start_line"],
                symbol["end_line"],
            ),
        )

    for start_line, end_line, chunk_text in chunk_lines(text):
        chunk_id = f"{relative_path}:{start_line}-{end_line}"
        connection.execute(
            """
            INSERT OR REPLACE INTO chunks(id, file_id, start_line, end_line, text)
            VALUES (?, ?, ?, ?, ?)
            """,
            (chunk_id, file_id, start_line, end_line, chunk_text),
        )
        connection.execute(
            "INSERT INTO chunks_fts(chunk_id, text) VALUES (?, ?)",
            (chunk_id, chunk_text),
        )

        collection.upsert(
            ids=[chunk_id],
            documents=[chunk_text],
            metadatas=[{
                "path": relative_path,
                "start_line": start_line,
                "end_line": end_line,
            }],
        )


def main():
    connection = setup_sqlite()
    chroma_client = chromadb.PersistentClient(path=str(CHROMA_DIR))
    collection = chroma_client.get_or_create_collection("code_chunks")

    for path in sorted(Path(SAMPLE_REPO).glob("**/*.py")):
        index_file(connection, collection, path)

    connection.commit()
    connection.close()

    print("Index created.")
    print(f"SQLite: {SQLITE_DB}")
    print(f"Chroma:  {CHROMA_DIR}")


if __name__ == "__main__":
    main()
