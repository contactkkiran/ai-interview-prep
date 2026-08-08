The context window is the maximum amount of text the model can look at in one request.

It includes:

- 🧩 system prompt
- 👤 user question
- 📝 chat history
- 📄 retrieved documents
- 🧪 tool results
- 🧠 model output

### Simple definition

```text
Context window = the model's working memory for a single request
```

The model cannot use information that is not inside its context window unless a tool or retrieval system provides it.
### Interview connection

A repo has 20M lines of code. That is far bigger than the context window, so the system needs retrieval, indexing, summaries, and code search.

Good answers should explain:

- why context windows exist
- why GPUs impose limits
- how token attention scales
- why larger context isn't always the answer
- sliding windows
- long-context models
- context compression
- hierarchical retrieval
