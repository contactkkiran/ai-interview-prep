## 11. What Is Grounding?

### 🧭 Core Idea

**Grounding** means forcing the model to base its answer on trusted information.

---

### 📚 Grounding Sources

- Retrieved documents
- Database records
- Tool outputs
- Verified sources
- Citations

---

### 🔄 Grounding Flow

```text
Database
API             ┐
Documents        │
Knowledge Graph   ├──►  Model  ──►  Grounded answer
Search            │
Tools           ┘
```

> **RAG** is one common grounding technique.

---

### ⚖️ Compare

| Approach | What It Does |
|---|---|
| **Grounding** | Constrains the model's answer to trusted, verifiable sources at query time |
| **Fine-tuning** | Bakes new knowledge/behavior into the model's weights during training |
| **RAG** | A specific grounding technique — retrieves relevant documents and feeds them into the context before generation |
