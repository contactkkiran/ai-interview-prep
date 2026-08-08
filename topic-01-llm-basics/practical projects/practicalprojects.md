# 🛠️ Part 5 — Practical Project

## 🚀 Topic 01 – LLM Basics

### 📘 Interview Question Series with Enhanced Solution

### 🧱 Project Structure
- Practical Project
- Repository Understanding Agent

### 🤖 Answer

💬 If I were answering the Tech Mahindra question in an interview, I would say:

🧠 I would not try to fit a 20-million-line repository into the model's context window. I would treat the repository as an indexed knowledge source and build a repository-understanding layer around the LLM.

🔍 First, I would parse the code structurally to create symbol and dependency information. Then I would combine lexical and semantic retrieval, because exact symbol matching and conceptual search solve different problems. I would maintain hierarchical summaries at repository, module, file, class, and function levels.

⚙️ At runtime, the coding agent would start with a small context and iteratively retrieve additional files, symbols, dependencies, and tests as required. Finally, I would use incremental indexing driven by repository changes so only affected code is reprocessed.

📊 I would also evaluate the retrieval layer independently using metrics such as Recall@K and MRR, because poor retrieval can cause an otherwise capable LLM to produce an incorrect answer.

### 🏆 Final Interview Answer

✅ So the fundamental solution isn't simply a larger context window. It is a combination of structured code indexing, hybrid retrieval, dependency-aware navigation, hierarchical summarization, iterative context construction, and incremental indexing.
