## 8. What Is Attention?

### 🧠 Core Idea

| Type | |
|---|---|
| Self-attention | Relates tokens within the same sequence to each other |
| Cross-attention | Relates tokens between two different sequences (e.g., encoder ↔ decoder) |
| Masked attention | Prevents a token from attending to future tokens (used during generation) |
| Multi-head attention | Runs several attention patterns in parallel |

Attention is the mechanism that lets the model **focus on relevant tokens**.

---

### 💡 Simple Idea

```text
For each token, attention asks:
"Which other tokens should I look at?"
```

---

### 🎤 Interview Connection

When someone asks *"Explain Transformer architecture,"* mention:

- ✅ Self-attention
- ✅ Multi-head attention
- ✅ Encoder/decoder structure
- ✅ Positional encoding
