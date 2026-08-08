## 7. What is a Transformer?

### 🤖 Core Idea

A Transformer is the main architecture behind modern LLMs.

You do not need the math first. Start with the idea:

```text
Transformer = a neural network architecture that learns relationships between tokens using attention
```

It helps the model decide which earlier tokens matter for predicting the next token.

### 🧠 Why It Matters

Example:

```text
The bank approved the loan because it trusted the customer.
```

The model needs to understand that "it" probably refers to "the bank", not "the loan".

### 🛠️ Build from Scratch

- RNN problems
- ↓
- LSTM problems
- ↓
- Transformer

### 🧩 Transformer Building Blocks

- Encoder
- Decoder
- Self-attention
- Multi-head attention
- Feed-forward layers
- Residual connections
- Layer normalization
- Output projection

### 👁️ Visual Intuition

I deposited money in the bank.

- bank
  - river?
  - financial?

Attention decides which meaning is relevant.

---
