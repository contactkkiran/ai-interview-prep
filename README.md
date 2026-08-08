# 🤖 Topic 01 — LLM Basics

## 🌟 Overview

This topic builds the foundation required to understand LLM-based
applications and answer AI Engineer interview questions confidently.

The goal is to learn each concept from first principles, connect it
to real engineering problems, and then apply it through interview
questions and practical projects.

---

## 📚 Lessons

### 📘 Lesson 01 — What Is an LLM?

- What is an LLM?
- How an LLM generates text
- Next-token prediction
- Examples of modern LLMs
- Basic LLM architecture

### 🪙 Lesson 02 — Tokens & Token Economics

- What is a token?
- Tokenization
- Input tokens
- Output tokens
- Token cost
- Token latency
- Why token count affects inference cost and speed

### 🧠 Lesson 03 — Context Window

- What is a context window?
- What goes inside the context window?
- Context limits
- Context and latency
- Context and cost
- Why larger context does not completely solve repository-scale problems

### 🔢 Lesson 04 — Embeddings

- What are embeddings?
- Semantic similarity
- Vector representations
- Similarity search
- Embeddings in RAG
- Embeddings in semantic caching

### 🧩 Lesson 05 — Transformers

- What is a Transformer?
- Encoder
- Decoder
- Self-attention
- Multi-head attention
- Feed-forward networks
- Residual connections
- Layer normalization

### 👁️ Lesson 06 — Attention

- What is attention?
- Self-attention
- Cross-attention
- Masked attention
- Multi-head attention
- Why attention matters

### 📝 Lesson 07 — Prompts

- What is a prompt?
- System prompts
- User prompts
- Application/developer prompts
- Zero-shot prompting
- Few-shot prompting
- Structured output
- Tool prompts
- Prompt injection

### ⚠️ Lesson 08 — Hallucinations

- What is hallucination?
- Why hallucinations happen
- Missing information
- Ambiguous questions
- Outdated information
- Poor retrieval
- Weak prompting
- Reducing hallucinations

### 🧭 Lesson 09 — Grounding

- What is grounding?
- Trusted information sources
- Documents
- Databases
- APIs
- Search
- Tools
- Grounding vs RAG vs fine-tuning

---

# 📝 Practice

Practice questions are maintained in:

`practice.md`

The practice is intentionally short.

The objective is to verify understanding rather than memorize long answers.

---

# 🎤 Interview Questions

Realistic company interview scenarios are maintained under:

`interview-questions/`

Current company scenarios include:

- Tech Mahindra — Repository-scale understanding
- Paytm — Multi-hop retrieval
- Virtusa — Tables in RAG
- ServiceNow — Semantic caching
- HDFC — Knowledge refresh
- Razorpay — Financial guardrails
- TCS — LLM inference
- Zapier — Agent framework selection

For each interview question, the goal is to understand:

1. The interview question
2. What the interviewer is testing
3. How to approach the problem
4. The supplied/source solution
5. Our deeper engineering solution
6. Production architecture
7. Common mistakes
8. Follow-up questions
9. Practical implementation

---

# 🎯 Interview Cheat Sheet

Short interview-ready answers are maintained in:

`interview-cheat-sheet.md`

These are not intended to replace understanding.

The objective is to develop the ability to explain the concept
clearly and concisely during an interview.

---

# 🗺️ Interview Question Map

The relationship between concepts and company interview questions
is maintained in:

`interview-question-map.md`

This connects:

Concept
→ Interview Question
→ Engineering Problem
→ Architecture
→ Practical Implementation

---

# 🛠️ Practical Projects

Practical implementations are maintained under:

`practical-projects/`

## Repository Understanding Agent

The first major practical project for Topic 01 is:

`practical-projects/repository-understanding-agent/`

This project is based on the repository-scale understanding problem
from the Tech Mahindra AI Engineer interview scenario.

### Problem

An AI coding assistant needs to understand repositories containing
millions of lines of code, while the complete repository cannot fit
inside an LLM context window.

### Project Goals

Build a repository-understanding system that progressively supports:

1. Read repository
2. Parse Python files
3. Create code chunks
4. Generate embeddings
5. Store embeddings in a vector database
6. Perform lexical search
7. Build a dependency graph
8. Generate hierarchical summaries
9. Build relevant context
10. Answer repository questions using an agent

The project will be developed gradually as the corresponding
LLM concepts are learned.

---

# 🎯 By the End of Topic 01

By the end of this topic, the learner should not simply know
definitions.

The goal is to understand:

- Why LLMs use tokens
- Why tokens affect cost and latency
- Why context windows have practical limits
- Why embeddings are useful
- How Transformers and attention work
- How prompts influence model behavior
- Why hallucinations occur
- How grounding improves reliability
- How these concepts appear in real AI Engineer interviews

The learner should also be able to connect these concepts to
real engineering problems.

For example:

```text
Context Window
      ↓
20M-Line Repository Problem
      ↓
Retrieval
      ↓
Code Indexing
      ↓
Semantic + Lexical Search
      ↓
Dependency Graph
      ↓
Context Construction
      ↓
Repository Understanding Agent


---

# 🎯 Topic 01 Outcome

By completing Topic 01, I should be able to:

- Explain LLM concepts from first principles.
- Explain tokens, token economics, and context windows.
- Explain embeddings, Transformers, and attention.
- Explain prompts, hallucinations, and grounding.
- Connect these concepts to real AI engineering problems.
- Answer senior-level AI Engineer interview questions confidently.
- Explain the architecture behind real interview scenarios.
- Build practical AI implementations rather than only memorizing answers.

## 🛠️ Practical Outcome

I will build a:

**Repository Understanding Agent**

based on the Tech Mahindra repository-scale AI coding assistant problem.

The project will demonstrate:

```text
LLM Basics
    ↓
Context Window
    ↓
Embeddings
    ↓
Retrieval
    ↓
Lexical + Semantic Search
    ↓
Code Indexing
    ↓
Dependency Graph
    ↓
Context Construction
    ↓
Repository Understanding Agent
