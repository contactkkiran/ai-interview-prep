## 2. What is a token?

A token is a small piece of text.

It can be:

- a word
- part of a word
- punctuation
- a space-like text unit

Example:

```text
"unbelievable" might become "un", "believ", "able"
```

### Why tokens matter

- 🟢 LLM cost is usually based on tokens
- 🟡 LLM speed depends on input and output token count
- 🔵 Context windows are measured in tokens

LLMs do not read full sentences the way humans do. They read tokens.

Tokens affect:

- 🟢 cost
- 🟡 speed
- 🔵 context window
- 🟠 memory limit
- 🔴 latency

### Key idea

More tokens = more work for the model = more cost + more latency
