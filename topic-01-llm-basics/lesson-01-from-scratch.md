# Lesson 01: LLM Basics From Scratch

## 1. What Is an LLM?

Before we talk about RAG, agents, caching, or inference systems, you must first understand:

- 🟢 What is an LLM?
- 🟡 What is a token?
- 🔵 What is a prompt?
- 🟠 What is a context window?
- 🔴 Why LLMs cost money
- 🟣 Why LLMs can be slow

LLM means Large Language Model.

It is a model trained on huge amounts of text so it can predict and generate text.

Simple idea:

```text
Input text → model → output text
```

AI models:

- 🔹 GPT
- 🔹 Claude
- 🔹 Llama
- 🔹 Gemini
- 🔹 Mistral

Example:

```text
Input: Explain RAG simply.
Output: RAG is a way to give an LLM external documents before it answers.
```

The model does not "know" like a human. It has learned patterns from training data and uses those patterns to generate likely next tokens.

Very simple example:

You type: `The capital of India is`
The model predicts: `New Delhi`

Because during training, it learned that this text pattern usually continues like that.

### Important interview line

> An LLM is a transformer-based model trained on massive text data to understand and generate natural language by predicting the next token.

---

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

---

## 3. Why does token count affect cost and speed?

The model must process every input token and generate every output token. More tokens mean more computation, more GPU time, and more cost.

### Interview perspective

A company needs a 70B open-source LLM serving 50,000 users daily.

If someone asks about serving 50,000 users cheaply and quickly, token count matters a lot.
The response must be under 2 seconds.
Infrastructure cost must stay low.

How would you design the inference system?

In that question, token count matters because:

- 🟢 more input tokens = more processing time
- 🟡 more output tokens = more generation time
- 🔵 more total tokens = more GPU usage
- 🔴 more GPU usage = higher cost

### Best answer outline

> For high-scale LLM serving, token count directly impacts latency and cost because every input and output token consumes GPU compute. Reducing unnecessary tokens is one of the first optimization steps.

---

## 4. Token optimization strategies

- 🧩 Prompt optimization
  - Pre-train reusable templates for common queries
  - Strip redundant instructions
  - Summarize long histories → feed only the essential context
- 🚀 Model serving strategy
  - Tensor/model parallelism → split a 70B model across GPUs
  - Pipeline parallelism → stream tokens as they’re generated
  - Speculative decoding → small draft model predicts tokens, large model verifies
- 📦 Caching layer
  - Cache frequent queries (FAQs)
  - Use embedding similarity search to reuse past answers
  - Avoid recomputation to save GPU cycles
- 🧠 RAG architecture
  - Store knowledge in a vector DB (FAISS, Milvus)
  - Retrieve only relevant snippets
  - Give the external LLM minimal context
- ⚡ Hardware efficiency
  - Use A100/H100 GPUs with FP8 quantization
  - Quantize weights (4-bit/8-bit)
  - Deploy with vLLM/FasterTransformer for optimized memory management
- 🌐 Load balancing
  - API gateway distributes requests
  - Autoscaling GPU clusters handle peak loads
  - Async batching → multiple requests per forward pass

### Example flow

1. 🧭 User query → API gateway
2. 🧠 Gateway checks cache → returns if hit
3. 🔎 If miss → retrieve context (RAG) → compress tokens
4. ✏️ Optimized prompt → LLM cluster (quantized, parallelized)
5. ⚡ Speculative decoding streams first tokens in <2s
6. ✅ Response returned → logged + cached

> Interview insight: Token count is the biggest lever for latency and cost. Every design choice (prompt compression, RAG, caching, batching, quantization) is about reducing tokens or making token processing cheaper and faster.

---

## 5. What is a context window?

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

---

## 6. What are embeddings?

Embeddings turn text into numeric vectors that capture meaning.

Example:

```text
"How do I reset my password?"
"I forgot my login password."
```

These sentences use different words but mean similar things. Their embeddings should be close to each other.

### Embeddings are used for:

- 🔍 semantic search
- 🧠 RAG
- 💾 semantic caching
- ⭐ recommendation systems
- 🔁 duplicate-question detection

### Topics to cover

- 💡 why embeddings exist
- 📏 dense vectors
- 🪸 sparse vectors
- 🤝 semantic similarity
- 📐 cosine similarity
- ➕ dot product
- 📏 Euclidean distance
- 📦 embedding dimensions
- 🧩 chunk embeddings
- 🗂 metadata

Then connect to:

- ServiceNow semantic cache
- Paytm multi-hop retrieval

### Interview connection

The semantic caching question depends directly on embeddings. You compare the new question's embedding with cached question embeddings.

---

## 7. What is a Transformer?

A Transformer is the main architecture behind modern LLMs.

You do not need the math first. Start with the idea:

```text
Transformer = a neural network architecture that learns relationships between tokens using attention
```

It helps the model decide which earlier tokens matter for predicting the next token.

Example:

```text
The bank approved the loan because it trusted the customer.
```

The model needs to understand that "it" probably refers to "the bank", not "the loan".

### Build from scratch

- RNN problems
- ↓
- LSTM problems
- ↓
- Transformer

### Transformer building blocks

- Encoder
- Decoder
- Self attention
- Multi-head attention
- Feed-forward layers
- Residual connections
- Layer normalization
- Output projection

### Visual intuition

I deposited money in the bank.

- bank
  - river?
  - financial?

Attention decides which meaning is relevant.

---

## 8. What is attention?

- Self attention
- Cross attention
- Masked attention
- Multi-head attention

Attention is the mechanism that lets the model focus on relevant tokens.

Simple idea:

```text
For each token, attention asks:
"Which other tokens should I look at?"
```

### Interview connection

When someone asks "Explain Transformer architecture", mention:

- self-attention
- multi-head attention
- encoder/decoder structure
- positional encoding

---

## 9. What is a prompt?

A prompt is the instruction or input you give the model.

### Prompt types

- system prompt: high-level rules or role
- user prompt: actual request
- developer/application prompt: desired app behavior
- examples: sample inputs and outputs

### Prompt quality affects

- accuracy
- tone
- structure
- safety
- tool usage

### Prompt patterns to cover

- zero-shot
- one-shot
- few-shot
- role prompting
- chain-of-thought
- ReAct
- structured output
- XML prompts
- JSON prompts
- tool prompts
- prompt injection

---

## 10. Why do hallucinations happen?

Hallucination means the model gives an answer that sounds confident but is wrong or unsupported.

### Common causes

- missing source information
- ambiguous questions
- outdated training data
- bad retrieval
- weak prompt constraints
- model guessing instead of saying "I do not know"

### How to avoid hallucinations

- ground answers in real data
- use retrieval or tools
- validate outputs
- add explicit constraints
- reduce temperature for better precision

### Interview connection

Questions about reducing hallucinations require grounding, retrieval, citations, validation, and sometimes human review.

---

## 11. What is grounding?

Grounding means forcing the model to base its answer on trusted information.

### Grounding sources

- retrieved documents
- database records
- tool outputs
- verified sources
- citations

### Grounding flow

- Database
- API
- Documents
- Knowledge Graph
- Search
- Tools

RAG is one common grounding technique.

### Compare

- Grounding
- Fine tuning
- RAG

---

## 12. Today's minimum interview answer

If an interviewer asks "What is an LLM?", a strong short answer is:

```text
An LLM is a Transformer-based model trained on large text datasets to predict and generate tokens. It works inside a context window, uses attention to relate tokens, and can be improved with prompts, retrieval, tools, and grounding to reduce hallucinations.
```

Do not memorize only this. Understand each phrase slowly.

---

## Company interview questions

This section shows realistic interview prompts inspired by actual industry scenarios.

Example companies:

- Tech Mahindra — Repository understanding
- Paytm — Multi-hop retrieval
- Virtusa — Tables in RAG
- ServiceNow — Semantic cache
- HDFC — Knowledge refresh
- Razorpay — Financial guardrails
- TCS — LLM inference
- Zapier — Agent framework selection

For each question, include:

- the question
- what the interviewer is testing
- how to think about it
- a senior-level answer
- common mistakes
- follow-up questions
- production architecture discussion

---

## Practical project

This is where your repository becomes unique.

Instead of stopping at "Context Window", we build a Repository Understanding Agent under `practical-projects`.

### Steps

1. Read repository
2. Parse Python files
3. Create chunks
4. Generate embeddings
5. Store in vector DB
6. Lexical search
7. Dependency graph
8. Summaries
9. Context builder
10. Repository Q&A agent

---

## By the end of Topic 01

Learners won't just know what a context window is — they'll understand why repository-scale AI assistants need retrieval, indexing, and code graphs, and they'll have built a working prototype.

### My goal for this repository

I don't want someone to finish this repository and say:

> I know LangChain.

I want them to finish it and say:

> I can explain AI concepts from first principles, answer senior AI interview questions confidently, design production-grade architectures, and demonstrate working implementations.

If we maintain this quality across all topics, I genuinely believe `ai-interview-prep` can become a standout GitHub repository for AI Engineer interview preparation — not because it covers the most topics, but because it teaches each topic deeply, practically, and in the context of real engineering interviews.
