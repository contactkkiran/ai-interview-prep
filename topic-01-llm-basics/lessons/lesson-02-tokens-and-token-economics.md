## 2. What Is a Token?

A **token** is a small piece of text.

It can be:

- a word
- part of a word
- punctuation
- a space-like text unit

### Example

```text
"unbelievable" might become "un", "believ", "able"
```

---

### Why Tokens Matter

| | Impact |
|---|---|
| 🟢 | LLM cost is usually based on tokens |
| 🟡 | LLM speed depends on input and output token count |
| 🔵 | Context windows are measured in tokens |

LLMs do not read full sentences the way humans do. **They read tokens.**

### Tokens Affect

| | Factor |
|---|---|
| 🟢 | Cost |
| 🟡 | Speed |
| 🔵 | Context window |
| 🟠 | Memory limit |
| 🔴 | Latency |

---

### 🎯 Key Idea

> **More tokens = more work for the model = more cost + more latency**
