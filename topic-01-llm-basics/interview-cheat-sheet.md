# 🎯 Topic 01 — LLM Basics Interview Cheat Sheet

This cheat sheet contains short interview-ready answers for the core concepts covered in Topic 01.

> ⚠️ **Do not memorize these answers blindly.**
> The goal is to understand every phrase and be able to explain it naturally during an interview.

---

## 1. 🤖 What Is an LLM?

### 🎯 Minimum Interview Answer

> An LLM is a Transformer-based model trained on large text datasets to predict and generate tokens. It works inside a context window, uses attention to relate tokens, and can be improved with prompts, retrieval, tools, and grounding to reduce hallucinations.

**🔑 Keywords:** Transformer · Tokens · Training data · Context window · Attention · Prompt · Retrieval · Grounding

**🎤 Possible Follow-ups**
- Why is it called a language model?
- Why is it called "large"?
- What is a token?
- How does an LLM generate text?
- What happens during inference?
- Does an LLM actually understand language?
- Why do LLMs hallucinate?

---

## 2. 🪙 What Is a Token?

### 🎯 Minimum Interview Answer

> A token is a unit of text processed by an LLM. A token can represent a complete word, part of a word, punctuation, or another text unit. Input and output are processed as tokens, which directly affects context usage, latency, and cost.

**🔑 Keywords:** Tokenization · Input tokens · Output tokens · Context · Cost · Latency

**🎤 Possible Follow-ups**
- Why don't LLMs process words directly?
- Why does token count affect cost?
- Why does token count affect latency?
- What is the difference between tokens and words?
- What happens when the context limit is exceeded?

---

## 3. 📦 What Is a Context Window?

### 🎯 Minimum Interview Answer

> A context window is the maximum amount of tokenized information an LLM can process as part of a request. It can include the system prompt, user input, conversation history, retrieved documents, tool results, and the model's response.

**🔑 Keywords:** Token limit · System prompt · User prompt · Chat history · Retrieved context · Tool results · Model output

**🎤 Possible Follow-ups**
- Why do context windows have limits?
- Does a larger context window solve every problem?
- How does context size affect latency?
- How does context size affect cost?
- How would you handle a 20M-line repository?

---

## 4. 🧠 What Are Embeddings?

### 🎯 Minimum Interview Answer

> Embeddings are numerical vector representations of data that capture semantic meaning. Text with similar meaning tends to have similar vector representations, making embeddings useful for semantic search, RAG, recommendations, duplicate detection, and semantic caching.

**🔑 Keywords:** Vector · Semantic meaning · Similarity · Semantic search · RAG · Vector database · Semantic cache

**🎤 Possible Follow-ups**
- What is cosine similarity?
- Why are embeddings useful for RAG?
- What is the difference between lexical and semantic search?
- What is embedding dimension?
- Why can semantic search fail?
- Why do we need metadata?

---

## 5. 🏗️ What Is a Transformer?

### 🎯 Minimum Interview Answer

> A Transformer is a neural network architecture that uses attention mechanisms to model relationships between tokens. Transformers form the foundation of most modern LLMs and support efficient processing of language compared with earlier sequence-based architectures.

**🔑 Keywords:** Attention · Self-attention · Encoder · Decoder · Multi-head attention · Feed-forward network · Positional information

**🎤 Possible Follow-ups**
- Why were Transformers introduced?
- What problem did they solve compared with RNNs?
- What is self-attention?
- What is multi-head attention?
- What is the difference between encoder and decoder?
- Why do modern LLMs mostly use Transformer architectures?

---

## 6. 🎯 What Is Attention?

### 🎯 Minimum Interview Answer

> Attention is a mechanism that allows a model to determine which tokens are more relevant to each other when processing a sequence. Self-attention allows tokens to relate to other tokens in the same sequence, while multi-head attention allows the model to learn different relationships in parallel.

**🔑 Keywords:** Query · Key · Value · Self-attention · Cross-attention · Multi-head attention

**🎤 Possible Follow-ups**
- What are Query, Key, and Value?
- What is self-attention?
- What is cross-attention?
- What is masked attention?
- Why do we need multiple attention heads?
- What is the computational cost of attention?

---

## 7. ✍️ What Is a Prompt?

### 🎯 Minimum Interview Answer

> A prompt is the instruction and contextual input provided to an LLM to guide its behavior and output. Effective prompts can define the task, constraints, context, expected format, examples, and available tools.

**🔑 Keywords:** System prompt · User prompt · Instructions · Context · Examples · Constraints · Structured output · Tools

**🎤 Possible Follow-ups**
- What is zero-shot prompting?
- What is few-shot prompting?
- What is role prompting?
- What is structured output?
- How do you improve prompt reliability?
- What is prompt injection?

---

## 8. ⚠️ What Is Hallucination?

### 🎯 Minimum Interview Answer

> Hallucination occurs when an LLM generates information that is incorrect, unsupported, or fabricated while presenting it as a plausible answer.

**🔑 Common Causes**
- Missing information
- Ambiguous questions
- Outdated knowledge
- Poor retrieval
- Weak prompts
- Model guessing
- Incorrect context

**🎤 Possible Follow-ups**
- How do you reduce hallucinations?
- Does lowering temperature eliminate hallucinations?
- Can RAG completely eliminate hallucinations?
- How do you detect hallucinations?
- What happens when retrieval fails?

---

## 9. 🛡️ What Is Grounding?

### 🎯 Minimum Interview Answer

> Grounding means providing an LLM with trusted, external information and constraining the response to that information. Grounding can use retrieved documents, databases, APIs, search systems, tools, or other verified sources.

**🔑 Keywords:** Trusted sources · Retrieval · Documents · Database · APIs · Tools · Citations · Verification

**🎤 Possible Follow-ups**
- How does RAG provide grounding?
- What happens when the retrieved information is wrong?
- What is the difference between grounding and fine-tuning?
- Can tools provide grounding?
- How would you validate grounded responses?

---

## 10. 💰 Why Do LLM Applications Become Expensive?

### 🎯 Minimum Interview Answer

> LLM cost is strongly influenced by the number of input and output tokens processed and the model used. Larger prompts, longer conversations, unnecessary retrieved context, and large outputs increase computation, latency, and cost.

**🔑 Optimization Techniques**
- ✅ Reduce unnecessary context
- ✅ Retrieve only relevant information
- ✅ Control output length
- ✅ Use appropriate models
- ✅ Cache repeated requests
- ✅ Batch workloads where appropriate
- ✅ Use smaller models where sufficient

---

## 11. 🏢 How Would You Handle a 20M-Line Repository?

### 🎯 Minimum Interview Answer

> I would not attempt to place the entire repository into the LLM context. I would treat the repository as a retrieval corpus and combine structured code indexing, lexical and semantic search, dependency graphs, hierarchical summaries, iterative context expansion, and incremental indexing.

### 🏗️ Core Architecture

```text
👨‍💻 Developer Task
        ↓
🧠 Query Analysis
        ↓
🔎 Lexical Search  +  🧠 Semantic Search
        ↓
🔷 Symbol / Code Index
        ↓
🕸️ Dependency Graph
        ↓
📊 Ranking / Re-ranking
        ↓
📦 Context Builder
        ↓
🤖 LLM
        ↓
💻 Answer / Code Change
```
