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

Examples of AI Models:

-GPT
-Claude
-Llama
-Gemini
-Mistral

Example :

```text
Input: Explain RAG simply.
Output: RAG is a way to give an LLM external documents before it answers.
```

The model does not "know" like a human. It has learned patterns from training data and uses those patterns to generate likely next tokens.

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

Interview connection:

If someone asks about serving 50,000 users cheaply and quickly, token count matters a lot.

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

## 6. What Is Attention?

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

RAG is one common grounding technique.

## 10. Today's Minimum Interview Answer

If an interviewer asks "What is an LLM?", a simple answer is:

```text
An LLM is a Transformer-based model trained on large text datasets to predict and generate tokens. It works inside a context window, uses attention to relate tokens, and can be improved with prompts, retrieval, tools, and grounding to reduce hallucinations.
```

Do not memorize only this. Understand each word slowly.
