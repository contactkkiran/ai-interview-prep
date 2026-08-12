## 3. What Is a Context Window?

The **context window** is the maximum amount of text the model can look at in one request.

### It Includes

| | Component |
|---|---|
| 🧩 | System prompt |
| 👤 | User question |
| 📝 | Chat history |
| 📄 | Retrieved documents |
| 🧪 | Tool results |
| 🧠 | Model output |

### Simple Definition

```text
Context window = the model's working memory for a single request
```

> The model cannot use information that is **not inside its context window**, unless a tool or retrieval system provides it.

---

### 🎯 Interview Connection

**Scenario:** A repo has 20M lines of code. That is far bigger than the context window, so the system needs retrieval, indexing, summaries, and code search.

Good answers should explain:

- ✅ Why context windows exist
- ✅ Why GPUs impose limits
- ✅ How token attention scales
- ✅ Why larger context isn't always the answer
- ✅ Sliding windows
- ✅ Long-context models
- ✅ Context compression
- ✅ Hierarchical retrieval
