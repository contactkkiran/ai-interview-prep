from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SAMPLE_REPO = PROJECT_ROOT / "data" / "sample_repo"
STORAGE_DIR = PROJECT_ROOT / "storage"
SQLITE_DB = STORAGE_DIR / "code_index.db"
CHROMA_DIR = STORAGE_DIR / "chroma"
SCHEMA_FILE = PROJECT_ROOT / "schema.sql"

