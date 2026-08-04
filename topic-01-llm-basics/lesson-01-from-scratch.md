# Lesson 01: LLM Basics From Scratch

## 1. What Is An LLM?

# Before we talk about RAG, agents, caching, or inference systems, you must first understand:


- What is an LLM?
- What is a token?
- What is a prompt?
- What is context window?
- Why LLMs cost money?
- Why LLMs can be slow?


LLM means Large Language Model.

It is a model trained on huge amounts of text so it can predict and generate text.

Simple idea:

```text
Input text -> model -> output text
```

AI Models:

- GPT
- Claude
- Llama
- Gemini
- Mistral

Example :

```text
Input: Explain RAG simply.
Output: RAG is a way to give an LLM external documents before it answers.
```

The model does not "know" like a human. It has learned patterns from training data and uses those patterns to generate likely next tokens.

Very Simple Example:

you type : The capital of India is
The model predicts: New Delhi

Because during training, it learned that this text pattern usually continues like that.

### Important Interview Line
    You can say:
    An LLM is a transformer-based model trained on massive text data to understand
    and generate natural language by predicting the next token.

## 2. What Is A Token?

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

Why tokens matter:

- LLM cost is usually based on tokens.
- LLM speed depends on input and output token count.
- Context windows are measured in tokens.

### why Tokens Matter:
    LLMs do not directly read full sentences like humans. They read tokens.
    Interview connection:

Tokens affect:
- cost
- speed
- context window
- memory limit
- latency
## Why does token count affect cost and speed?
Token count affects cost and speed because the model has to process every input token and generate every output token. More tokens mean more computation, higher cost, and slower response.

### Keep this in your head:
    More tokens = more work for model = more cost + more latency

## Interview perspective :
    ### A company needs a 70B open-source LLM serving 50,000 users daily
        or If someone asks about
        serving 50,000 users cheaply and quickly, token count matters a lot.
        Response must be under 2 seconds.
        Infrastructure cost must stay low.
    How would you design the inference system?
    In that question, token count matters because:
        more input tokens = more processing time
        more output tokens = more generation time
        more total tokens = more GPU usage
        more GPU usage = higher cost
    Answer :
        For high-scale LLM serving, token count directly impacts latency and cost because every input and output token consumes GPU compute. Reducing unnecessary tokens is one of the first optimization steps.

## 3. What Is A Context Window?

The context window is the maximum amount of text the model can look at in one request.

It includes:

- system prompt
- user question
- chat history
- retrieved documents
- tool results
- model output

Simple example:

```text
Context window = the model's temporary working memory for this request
```

Important point:

The model cannot use information that is not inside its context window unless it has a tool or retrieval system to fetch it.

Interview connection:

The coding-agent question says a repo has 20M lines of code. That is far bigger than a context window, so the system needs retrieval, indexing, summaries, and code search.

Instead of only saying
Context Window = memory

We'll explain
Why context windows exist
Why GPUs impose limits
How token attention scales
Why larger context isn't always the answer
Sliding windows
Long-context models
Context compression
Hierarchical retrieval

## 4. What Are Embeddings?

Embeddings turn text into numbers that capture meaning.

Example:

```text
"How do I reset my password?"
"I forgot my login password."
```

These sentences use different words but mean similar things. Their embeddings should be close to each other.

Embeddings are used for:

- semantic search
- RAG
- semantic caching
- recommendation systems
- duplicate-question detection

We'll cover
- Why embeddings exist
- Dense vectors
- Sparse vectors
- Semantic similarity
- Cosine similarity
- Dot product
- Euclidean distance
- Embedding dimensions
- Chunk embeddings
- Metadata
- Then connect to
- ServiceNow Semantic Cache
   and
- Paytm Multi-hop Retrieval

Interview connection:

The semantic caching question depends directly on embeddings. You compare the new question's embedding with cached question embeddings.

## 5. What Is A Transformer?

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


We'll explain
  Not just
  Transformer uses Attention
We'll build from scratch:
    RNN Problems

↓

LSTM Problems

↓

Transformer

↓

Encoder

↓

Decoder

↓

Self Attention

↓

Multi Head

↓

Feed Forward

↓

Residual Connections

↓

Layer Norm

↓

Output

Attention
We'll explain visually

I deposited money in the bank.

↓

bank

↓

River?

Financial?

↓

Attention determines this.
## 6. What Is Attention?

- Self Attention
- Cross Attention
- Masked Attention
- Multi Head Attention

Attention is the mechanism that lets the model focus on relevant tokens.

Simple idea:

```text
For each token, attention asks:
"Which other tokens should I look at?"
```

Interview connection:

When someone asks "Explain Transformer architecture", you must mention self-attention, multi-head attention, encoders/decoders, and positional information.

## 7. What Is A Prompt?

A prompt is the instruction or input you give the model.

- Instead of saying
- Prompt = input
- We'll cover
- Zero-shot
- One-shot
- Few-shot
- Role prompting
- Chain of Thought
- ReAct
- Structured Output
- XML prompts
- JSON prompts
- Tool prompts
- Prompt Injection

Types:

- system prompt: high-level rules or role
- user prompt: user's actual request
- developer/application prompt: app-specific behavior
- examples: sample inputs and outputs

Prompt quality affects:

- accuracy
- tone
- structure
- safety
- tool usage

## 8. Why Do Hallucinations Happen?

Hallucination means the model gives an answer that sounds confident but is wrong or unsupported.

Common causes:

- missing source information
- ambiguous question
- outdated training data
- bad retrieval
- weak prompt constraints
- model guessing instead of saying "I do not know"

How to avoid them
- Topics include:
- Missing knowledge
- Weak grounding
- Retrieval failure
- Prompt ambiguity
- Model confidence
- Temperature effects

Interview connection:

Questions about reducing hallucinations require grounding, retrieval, citations, validation, and sometimes human review.

## 9. What Is Grounding?

Grounding means forcing the model to base its answer on trusted information.

Examples:

- retrieved documents
- database records
- tool outputs
- verified sources
- citations

Different grounding sources
Database

↓

API

↓

Documents

↓

Knowledge Graph

↓

Search

↓

Tools

RAG is one common grounding technique.

Then compare :
    Grounding
    vs
    Fine Tuning
    vs
    RAG


## 10. Today's Minimum Interview Answer

If an interviewer asks "What is an LLM?", a simple answer is:

```text
An LLM is a Transformer-based model trained on large text datasets to predict and generate tokens. It works inside a context window, uses attention to relate tokens, and can be improved with prompts, retrieval, tools, and grounding to reduce hallucinations.
```

Do not memorize only this. Understand each word slowly.

###Company Interview Questions
I think this will be the most valuable section.
Instead of generic questions, we'll include realistic interview prompts inspired by actual industry scenarios.
Example:
    Tech Mahindra
        Repository Understanding
    Paytm
       Multi-hop Retrieval
    Virtusa
       Tables in RAG
    ServiceNow
        Semantic Cache
    HDFC
        Knowledge Refresh
    Razorpay
        Financial Guardrails
    TCS
        LLM Inference
    Zapier
        Agent Framework Selection

For each one, we'll include:
- The question
- What the interviewer is really testing
- How to think about it
- A senior-level answer
- ommon mistakes
- Follow-up questions
- A production architecture discussion

# Practical Project
This is where your repository becomes unique.
Instead of stopping at
    Context Window
we immediately build Repository Understanding Agent under 'practical- projects' dir

Step 1

Read Repository

↓

Step 2

Parse Python Files

↓

Step 3

Create Chunks

↓

Step 4

Generate Embeddings

↓

Step 5

Store in Vector DB

↓

Step 6

Lexical Search

↓

Step 7

Dependency Graph

↓

Step 8

Summaries

↓

Step 9

Context Builder

↓

Step 10

Repository Q&A Agent

## By the end of Topic 01, learners won't just know what a context window is—they'll understand why repository-scale AI assistants need retrieval, indexing, and code graphs, and they'll have built a working prototype.

### My goal for this repository
I don't want someone to finish this repository and say:
"I know LangChain."

I want them to finish it and say:

"I can explain AI concepts from first principles, answer senior AI interview questions confidently, design production-grade architectures, and demonstrate working implementations."

If we maintain this quality across all topics, I genuinely believe ai-interview-prep can become a standout GitHub repository for AI Engineer interview preparation—not because it covers the most topics, but because it teaches each topic deeply, practically, and in the context of real engineering interviews

text
