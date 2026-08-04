import sqlite3
import sys
import re

import chromadb

from config import CHROMA_DIR, SQLITE_DB


def search_semantic(question):
    chroma_client = chromadb.PersistentClient(path=str(CHROMA_DIR))
    collection = chroma_client.get_or_create_collection("code_chunks")
    results = collection.query(query_texts=[question], n_results=3)

    matches = []
    for index, chunk_id in enumerate(results["ids"][0]):
        matches.append({
            "chunk_id": chunk_id,
            "document": results["documents"][0][index],
            "metadata": results["metadatas"][0][index],
        })
    return matches


def search_exact(question):
    terms = re.findall(r"[A-Za-z_][A-Za-z0-9_]*", question)
    fts_query = " OR ".join(terms[:8])
    if not fts_query:
        return []

    connection = sqlite3.connect(SQLITE_DB)
    rows = connection.execute(
        """
        SELECT chunk_id, snippet(chunks_fts, 1, '[', ']', '...', 10)
        FROM chunks_fts
        WHERE chunks_fts MATCH ?
        LIMIT 3
        """,
        (fts_query,),
    ).fetchall()
    connection.close()
    return rows


def main():
    if len(sys.argv) < 2:
        print('Usage: python src/query_repo.py "your question"')
        return

    question = sys.argv[1]

    print("\nSemantic search results:")
    for match in search_semantic(question):
        metadata = match["metadata"]
        print(f"- {metadata['path']} lines {metadata['start_line']}-{metadata['end_line']}")

    print("\nExact search results:")
    for chunk_id, snippet in search_exact(question):
        print(f"- {chunk_id}: {snippet}")


if __name__ == "__main__":
    main()
