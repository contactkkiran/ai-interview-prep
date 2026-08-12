# 📘 Lesson 01: LLM Basics From Scratch

---

## 1. What Is an LLM?

Before we talk about RAG, agents, caching, or inference systems, you must first understand:

| | Concept |
|---|---|
| 🟢 | What is an LLM? |
| 🟡 | What is a token? |
| 🔵 | What is a prompt? |
| 🟠 | What is a context window? |
| 🔴 | Why LLMs cost money |
| 🟣 | Why LLMs can be slow |

**LLM** means **Large Language Model**.

It is a model trained on huge amounts of text so it can predict and generate text.

### Simple Idea

```text
Input text → model → output text
```

### Common LLMs

- 🔹 GPT
- 🔹 Claude
- 🔹 Llama
- 🔹 Gemini
- 🔹 Mistral

### Example

```text
Input:  Explain RAG simply.
Output: RAG is a way to give an LLM external documents before it answers.
```

---

## 2. How an LLM "Thinks"

The model does not "know" things the way a human does. It has learned **patterns** from training data and uses those patterns to generate the **likely next token**.

### Very Simple Example

> You type: `The capital of India is`
> The model predicts: `New Delhi`

Because during training, it learned that this text pattern usually continues that way.

---

## 🎯 Important Interview Line

> *"An LLM is a transformer-based model trained on massive text data to understand and generate natural language by predicting the next token."*
