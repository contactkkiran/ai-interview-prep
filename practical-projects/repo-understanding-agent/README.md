# Repo Understanding Agent

Practical project for this interview question:

```text
Your coding assistant must understand repositories with 20M lines of code.
Context windows are nowhere near big enough.
How do you build repository-scale understanding for coding agents?
```

## Goal

Build a small local system that:

- reads a code repository
- creates chunks from files
- extracts symbols like classes and functions
- stores exact-search metadata in SQLite
- stores semantic-search vectors in Chroma
- retrieves only relevant code instead of sending the whole repo to the LLM

## Why This Project Exists

An LLM cannot read a huge repository in one request.

So we do this:

```text
large repo -> index -> search -> relevant files/snippets -> LLM context
```

This is the practical meaning of:

```text
Retrieve, don't stuff.
```

## Folder Structure

```text
repo-understanding-agent/
├── README.md
├── requirements.txt
├── schema.sql
├── data/
│   └── sample_repo/
│       ├── app.py
│       ├── payments.py
│       └── users.py
├── storage/
│   └── .gitkeep
└── src/
    ├── config.py
    ├── index_repo.py
    ├── query_repo.py
    └── symbol_extractor.py
```

## Install

Run these commands from this folder:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Build The Index

```bash
python src/index_repo.py
```

This creates:

```text
storage/code_index.db
storage/chroma/
```

## Ask A Question

```bash
python src/query_repo.py "Where is payment processing handled?"
```

Expected idea:

```text
The system should retrieve payments.py, not the whole repo.
```

## Interview Answer Shape

```text
I would not put the entire 20M-line repository into the LLM context.
I would build an indexing and retrieval layer.
The system stores code chunks, symbols, dependencies, and summaries.
At query time, it retrieves only relevant files, functions, and snippets into the context window.
```

