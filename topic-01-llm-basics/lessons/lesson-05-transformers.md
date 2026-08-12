## 7. What Is a Transformer?

### 🤖 Core Idea

A **Transformer** is the main architecture behind modern LLMs.

You do not need the math first. Start with the idea:

```text
Transformer = a neural network architecture that learns relationships between tokens using attention
```

It helps the model decide which earlier tokens matter for predicting the next token.

---

### 🧠 Why It Matters

**Example:**

```text
The bank approved the loan because it trusted the customer.
```

The model needs to understand that **"it"** probably refers to **"the bank"**, not "the loan."

---

### 🛠️ Build From Scratch

```text
RNN problems
    ↓
LSTM problems
    ↓
Transformer
```

---

### 🧩 Transformer Building Blocks

| Block | Role |
|---|---|
| Encoder | Processes the input sequence |
| Decoder | Generates the output sequence |
| Self-attention | Relates tokens to each other within a sequence |
| Multi-head attention | Runs several attention patterns in parallel |
| Feed-forward layers | Transforms each token's representation |
| Residual connections | Preserve information across layers |
| Layer normalization | Stabilizes training |
| Output projection | Maps internal representation to output tokens |

---

### 👁️ Visual Intuition

> *"I deposited money in the **bank**."*

| "bank" could mean | |
|---|---|
| 🌊 | River (bank of a river)? |
| 🏦 | Financial (a bank)? |

**Attention decides which meaning is relevant** — using surrounding context ("deposited money") to resolve the ambiguity.
