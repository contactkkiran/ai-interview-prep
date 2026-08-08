# 💼 Tech Mahindra — Repository-Scale Understanding

## 🎯 Interview Question by Tech Mahindra

💡 Interview Note: Keep the interview answer high-level and follow the end-to-end flow; the detailed explanation is provided for reference and deeper understanding.

Your AI coding assistant must understand repositories with 20 million lines of code. Context windows are nowhere near large enough. How do you build repository-scale understanding for coding agents?


## 🟢 Part 1 — Tech Mahindra interview  Solution

💡 Their six points are the core architecture:

### 1️⃣ Retrieve, don't stuff

🧠 Treat the repository as a retrieval corpus.

20M LOC
   ↓
Repository Index
   ↓
Relevant files / symbols / snippets
   ↓
LLM Context

Don't send the entire repository to the LLM.

### 2️⃣ Index code by structure

🧱 Build:

Definitions
References
Imports
Call Graph
Dependency Graph
Symbols

The agent needs to understand relationships, not just text similarity.

### 3️⃣ Combine semantic + lexical search

🔍

🧠 Semantic Search
        +
🔎 Lexical / Symbol Search
        ↓
      Retrieval

Embeddings are good for conceptual similarity.

Lexical search is good for exact identifiers.

### 4️⃣ Summarize at multiple levels

📝 Create:

Repository Summary
       ↓
Module Summary
       ↓
File Summary
       ↓
Class Summary
       ↓
Function Summary

The agent can navigate from coarse → fine.

### 5️⃣ Expand context iteratively

🔄 Start with a small context.

Then:

Need more information?
        ↓
Follow import
        ↓
Find implementation
        ↓
Find caller
        ↓
Find tests

This is much better than sending everything initially.

### 6️⃣ Incremental indexing

⚡ When a developer changes:

PaymentService.java

don't rebuild the entire 20M-line index.

Instead:

Changed File
    ↓
Re-parse
    ↓
Re-embed
    ↓
Update symbols
    ↓
Update dependencies
    ↓
Update summaries

---

## 🔵 Part 2 — Where my Solution Goes Beyond

The important distinction:

Tech Mahindra gives the architectural principles.

We can go deeper into how we would actually engineer those principles.

For example:

### 1. AST-Based Code Indexing

💡 Tech Mahindra says:

🧱 Index code by structure.

🛠️ We can explain how.

Instead of treating:

PaymentService.java

as a text document, parse it using an AST/parser.

Extract:

Class:
PaymentService

Methods:
processPayment()
validatePayment()
refundPayment()

Imports:
PaymentRepository

Calls:
PaymentRepository.save()

References:
OrderService

Now our index understands the code structure.

### 2. Symbol-Level Retrieval

💡 Tech Mahindra Interview solution says:

🔷 Pull relevant files, symbols and snippets.

🧩 We can implement this at symbol level.

Instead of:

Retrieve entire PaymentService.java

retrieve:

PaymentService.processPayment()

plus the dependencies required to understand it.

This reduces:

Context size
Latency
Token cost
Irrelevant information

### 3. Hybrid Retrieval Pipeline

💡 Tech Mahindra Interview solution says:

🔎 Combine semantic and lexical search.

🧠 We can make the architecture explicit:

                 User Task
                    │
          ┌─────────┴─────────┐
          ▼                   ▼
    🔎 Lexical Search    🧠 Semantic Search
          │                   │
          └─────────┬─────────┘
                    ▼
               Candidate Set
                    │
                    ▼
                Re-Ranker
                    │
                    ▼
             Top Relevant Code

We can then discuss:

BM25
Symbol search
Embedding search
Metadata filtering
Re-ranking

### 4. Code Dependency Graph

💡 Tech Mahindra Interview solution says:

🕸️ Build a symbol/dependency graph.

🧱 Our implementation can model:

PaymentController
       │
       ▼
PaymentService
       │
       ├──────────────┐
       ▼              ▼
PaymentValidator   PaymentRepository
                       │
                       ▼
                   Database

Now the agent can answer:

"Where does payment validation happen?"

and follow the actual execution/dependency path.

### 5. Hierarchical Context

💡 Tech Mahindra says:

📝 Summarize at multiple levels.

🏗️ We can implement:

🏢 Repository
      │
      ▼
📦 Module
      │
      ▼
📄 File
      │
      ▼
🔷 Class
      │
      ▼
⚙️ Function
      │
      ▼
📝 Code

The agent doesn't immediately consume raw code.

It navigates the repository hierarchy first.

### 6. Agentic Retrieval

🤖 This is where we can go significantly deeper.

Instead of:

Question
   ↓
Search
   ↓
Answer

our coding agent can perform:

👨‍💻 Developer Task
        ↓
🧠 Planning
        ↓
🔍 Search
        ↓
📄 Inspect File
        ↓
🕸️ Follow Dependency
        ↓
🔍 Search Again
        ↓
🧪 Inspect Tests
        ↓
📦 Build Final Context
        ↓
🤖 LLM

The agent decides what additional context it needs.

That directly implements Tech Mahindra interview solution:

"Expand context iteratively as the agent works."

### 7. Retrieval Evaluation

📊 This is an important engineering layer we can add.

We should measure whether retrieval is actually working.

For example:

Recall@K
Precision@K
MRR
Context Precision
Context Recall

Suppose the correct implementation is in:

PaymentService.java

but our retriever returns:

PaymentController.java
PaymentDTO.java
PaymentMapper.java

The LLM may fail even though the LLM itself is excellent.

So:

Bad retrieval → bad answer.

### 8. Incremental Indexing + CI/CD

💡 Tech Mahindra says:

⚡ Re-index only changed files on commit.

🔄 We can turn this into a real pipeline:

👨‍💻 Git Commit
      ↓
🔍 Detect Changed Files
      ↓
🌳 Parse AST
      ↓
🧠 Generate Embeddings
      ↓
🕸️ Update Graph
      ↓
📝 Update Summaries
      ↓
🗄️ Update Index
      ↓
✅ Repository Ready

This could run as part of CI/CD.

---

## 🟣 Part 3 — Relationship Between the Two Approaches

💡 This is the most important point:

          TECH MAHINDRA
       Proposed Architecture
                │
                ▼
       ┌─────────────────┐
       │ Retrieve        │
       │ Code Graph      │
       │ Hybrid Search   │
       │ Summaries       │
       │ Iterative       │
       │ Incremental     │
       └────────┬────────┘
                │
                ▼
          OUR DEEP DIVE
                │
       ┌────────┼────────┐
       ▼        ▼        ▼
      AST    Re-ranking  Agent
       │        │        │
       ▼        ▼        ▼
   Symbols   Evaluation  Tools
       │        │        │
       └────────┼────────┘
                ▼
       🛠️ Working Project

Therefore:

Tech Mahindra's answer = architecture principles.

Our solution = architecture + implementation + engineering trade-offs + evaluation + working project.

We should preserve all six Tech Mahindra points exactly as the source/expected approach, then put our deeper implementation underneath each point.

That is the correct approach for our ai-interview-prep repository.

---

## 🟡 Part 4 — Is the Tech Mahindra Answer Ambiguous?

⚠️ Yes — the Tech Mahindra solution is somewhat high-level/ambiguous if the interviewer expects an implementation-level answer, but it is architecturally correct.

I would characterize it as:

🟢 Correct architecture principles
🟡 High-level implementation guidance
🔴 Not sufficient by itself for a deep AI Engineer/System Design interview

### Where it is ambiguous

| Tech Mahindra statement | What is missing |
| --- | --- |
| Retrieve, don't stuff | How do we retrieve? What index? What chunking strategy? |
| Index code by structure | Which parser/AST? How is the graph stored? |
| Semantic + lexical search | Which algorithms? How are results combined/ranked? |
| Summarize at multiple levels | How are summaries generated and updated? |
| Expand context iteratively | Who decides what to retrieve next? Rules or an agent? |
| Incremental indexing | How do we detect changes and update dependent symbols? |

So I would not call the answer wrong or vague. It's actually a very good architectural blueprint.

But if the interviewer asks:

💬 "Okay, design it."

then you need to go one level deeper.

For example:

Tech Mahindra says:

Combine semantic and lexical search.

Our interview answer should continue:

User Task
   ↓
Query / Intent Analysis
   ↓
 ┌───────────────┬────────────────┐
 │               │                │
 ▼               ▼                ▼
Lexical       Semantic        Symbol Search
(BM25)        Embeddings       (AST)
 │               │                │
 └───────────────┴────────────────┘
                 ↓
             Re-ranking
                 ↓
        Dependency Expansion
                 ↓
          Context Builder
                 ↓
                LLM

Then explain why each layer exists.

---

## 🎯 Part 5 — The Important Interview Distinction

💡 If you answer only with the Tech Mahindra six points:

Good answer — probably enough to demonstrate that you understand the architecture.

If you answer:

✅ Six principles + architecture + data structures + retrieval strategy + indexing strategy + agentic context expansion + evaluation + scalability/trade-offs

then you're giving a Senior/Staff-level answer.

And this is exactly what we should teach in ai-interview-prep:

Don't replace the company's answer. Decode it.

💼 Company Answer
       ↓
🧠 What does each statement actually mean?
       ↓
🏗️ How would I implement it?
       ↓
⚖️ What are the trade-offs?
       ↓
🛠️ Build a working version
       ↓
🎤 Handle follow-up questions

That will make the Tech Mahindra question much more valuable than simply memorizing those six bullets.

---

## 🛠️ Part 6 — Practical Project

### 🚀 Topic 01 – LLM Basics

### 🧱 Project Structure

Interview question series with my enhanced solution.

Practical project:

### 🤖 Answer

If I were answering the Tech Mahindra question in an interview, I would say:

I would not try to fit a 20-million-line repository into the model's context window. I would treat the repository as an indexed knowledge source and build a repository-understanding layer around the LLM.

First, I would parse the code structurally to create symbol and dependency information. Then I would combine lexical and semantic retrieval, because exact symbol matching and conceptual search solve different problems. I would maintain hierarchical summaries at repository, module, file, class, and function levels.

At runtime, the coding agent would start with a small context and iteratively retrieve additional files, symbols, dependencies, and tests as required. Finally, I would use incremental indexing driven by repository changes so only affected code is reprocessed.

I would also evaluate the retrieval layer independently using metrics such as Recall@K and MRR, because poor retrieval can cause an otherwise capable LLM to produce an incorrect answer.

### 🏆 Final Interview Answer

So the fundamental solution isn't simply a larger context window. It is a combination of structured code indexing, hybrid retrieval, dependency-aware navigation, hierarchical summarization, iterative context construction, and incremental indexing.

No single retrieval technique is sufficient.

🔎 Lexical Search

Useful for exact matches:

PaymentService
processPayment()
customerId
getTransaction()
🧠 Semantic Search

Useful for conceptual relationships.

For example:

"How do I authenticate a customer?"

could retrieve code related to:

login
authentication
identity verification
JWT validation
session management

even when the exact words don't match.

Therefore:

🔎 Lexical Search
        +
🧠 Semantic Search
        ↓
Better Retrieval
4️⃣ Summarize at Multiple Levels

A 5,000-line file should not necessarily be placed into the model context.

Instead, create summaries at different levels.

🏢 Repository
      │
      ▼
📦 Module
      │
      ▼
📄 File
      │
      ▼
🔷 Class
      │
      ▼
⚙️ Function

The coding agent can first understand the high-level structure and then drill down into the specific implementation it needs.

This creates a hierarchical understanding of the repository.

5️⃣ Expand Context Iteratively

Don't retrieve everything at the beginning.

Start with a narrow context.

Then allow the agent to request additional information when necessary.

For example:

👨‍💻 Developer Task
        │
        ▼
🔍 Find PaymentService
        │
        ▼
📄 Inspect implementation
        │
        ▼
🔗 Follow imported dependency
        │
        ▼
📄 Open PaymentRepository
        │
        ▼
🧪 Find relevant tests
        │
        ▼
📦 Build final context

The context grows as needed, rather than being front-loaded.

6️⃣ Cache and Update the Index Incrementally

A 20-million-line repository cannot be completely re-indexed for every request.

When a developer changes:

PaymentService.java

we should identify the changed portion and update the relevant indexes.

Conceptually:

👨‍💻 Git Commit
      │
      ▼
🔍 Detect Changed Files
      │
      ▼
🌳 Re-index Changed Code
      │
      ├── 🧠 Embeddings
      ├── 🔷 Symbols
      ├── 🕸️ Dependencies
      └── 📝 Summaries
      │
      ▼
🗄️ Updated Repository Index

This keeps the repository knowledge current without rebuilding everything.

🎯 Tech Mahindra's Core Lesson

The supplied answer concludes with an important principle:

You don't fit a 20-million-line repository into a context window. You build a retrieval and code-graph layer around it.

Repository-scale understanding is therefore primarily a:

🔍 Search Problem
        +
🗂️ Indexing Problem
        +
🕸️ Code Relationship Problem

rather than simply a:

📦 Bigger Context Window Problem

A larger context window may help, but it does not fundamentally solve repository-scale understanding.

🟡 Part 2 — Is the Tech Mahindra Answer Ambiguous?

The answer is architecturally correct, but it is intentionally high-level.

It tells us WHAT should be done, but doesn't fully specify HOW to implement it.

For example:

Tech Mahindra says:

Index code by structure.

The natural follow-up questions are:

How do we parse source code?
How do we extract symbols?
How do we build the dependency graph?
Where do we store the graph?
How do we update it?
How do we handle multiple programming languages?
Tech Mahindra says:

Combine semantic and lexical search.

Follow-up questions:

Which lexical search algorithm?
Which embedding model?
How do we combine the results?
How do we rank them?
How many results should we retrieve?
How do we prevent irrelevant code from entering the context?
Tech Mahindra says:

Expand context iteratively.

Follow-up questions:

Who decides what to retrieve next?
An LLM?
A deterministic retrieval policy?
An agent?
How do we prevent infinite retrieval?
How do we control token cost?

So the answer isn't wrong or vague.

It is best understood as a high-level architectural blueprint.

🔵 Part 3 — Our Proposed Engineering Solution

Our solution does not replace Tech Mahindra's answer.

It goes one level deeper:

Tech Mahindra's answer = architectural principles.

Our solution = those principles converted into an implementable production architecture.

🏗️ Proposed Architecture
                         👨‍💻 Developer
                              │
                              ▼
                        🎯 Coding Task
                              │
                              ▼
                       🧠 Query Analyzer
                              │
                ┌─────────────┼─────────────┐
                │             │             │
                ▼             ▼             ▼
          🔎 Lexical     🧠 Semantic    🔷 Symbol
             Search         Search        Search
                │             │             │
                └─────────────┼─────────────┘
                              ▼
                       📊 Candidate Ranking
                              │
                              ▼
                         🔄 Re-Ranker
                              │
                              ▼
                       🕸️ Dependency Graph
                              │
                              ▼
                     📚 Context Builder
                              │
             ┌────────────────┼────────────────┐
             │                │                │
             ▼                ▼                ▼
         📄 Code          📝 Summary       🔗 Dependencies
             │                │                │
             └────────────────┼────────────────┘
                              ▼
                           🤖 LLM
                              │
                              ▼
                     💻 Generated Answer
🔍 Step 1 — AST-Based Code Indexing

Tech Mahindra says:

Index code by structure.

Our implementation can use AST/parsing technology to understand source code structurally.

Instead of storing:

PaymentService.java

as one giant text document, extract:

🔷 Class
PaymentService

⚙️ Methods
processPayment()
validatePayment()
refundPayment()

📦 Imports
PaymentRepository

📞 Calls
PaymentRepository.save()

🔗 References
OrderService

This enables symbol-level retrieval.

🔷 Step 2 — Symbol-Level Retrieval

Instead of retrieving:

📄 Entire 5,000-line file

retrieve:

⚙️ PaymentService.processPayment()

and the specific dependencies required to understand it.

This reduces:

💰 Token cost
⏱️ Latency
🧠 Context pressure
❌ Irrelevant information
🔎 Step 3 — Hybrid Retrieval

We can implement:

                 User Task
                    │
          ┌─────────┴─────────┐
          ▼                   ▼
     🔎 Lexical          🧠 Semantic
       Search              Search
          │                   │
          └─────────┬─────────┘
                    ▼
             Candidate Set
                    │
                    ▼
               📊 Re-Ranker
                    │
                    ▼
              Top Candidates

Lexical retrieval is particularly valuable for:

Exact class names
Function names
Variables
Error messages
Configuration keys

Semantic retrieval is useful for:

Conceptual similarity
Business logic
Related implementations
Natural-language descriptions
🕸️ Step 4 — Dependency Graph

Represent repository relationships as a graph.

For example:

PaymentController
        │
        ▼
PaymentService
        │
   ┌────┴────┐
   ▼         ▼
Validator  Repository
              │
              ▼
           Database

The agent can then traverse the graph to find relevant context.

📝 Step 5 — Hierarchical Summaries

Create summaries at different levels:

Repository Summary
       ↓
Module Summary
       ↓
File Summary
       ↓
Class Summary
       ↓
Function Summary
       ↓
Raw Code

The agent can use the summary first and retrieve raw code only when necessary.

🤖 Step 6 — Agentic Context Expansion

Instead of retrieving everything at once:

Question
   ↓
Retrieve
   ↓
Answer

we can allow the coding agent to perform an iterative workflow:

👨‍💻 Task
   ↓
🧠 Plan
   ↓
🔍 Search
   ↓
📄 Inspect
   ↓
🕸️ Follow Dependency
   ↓
🔍 Search Again
   ↓
🧪 Inspect Tests
   ↓
📦 Build Context
   ↓
🤖 Generate Answer

This directly implements Tech Mahindra's "expand context iteratively" principle.

📊 Step 7 — Retrieval Evaluation

This is an additional engineering layer.

A powerful LLM cannot compensate for poor retrieval.

For example:

Expected:
PaymentService.java

Retrieved:
PaymentController.java
PaymentDTO.java
PaymentMapper.java

The model may fail because the correct code never reached its context.

Therefore, evaluate retrieval using metrics such as:

Recall@K
Precision@K
MRR
Context Precision
Context Recall

The exact metrics we use will depend on the retrieval task.

🔄 Step 8 — Incremental Indexing

Build an indexing pipeline around Git changes:

👨‍💻 Git Commit
      ↓
🔍 Detect Changes
      ↓
🌳 Parse Changed Files
      ↓
🔷 Update Symbols
      ↓
🧠 Update Embeddings
      ↓
🕸️ Update Dependencies
      ↓
📝 Update Summaries
      ↓
🗄️ Update Index

This avoids rebuilding the 20-million-line repository index after every commit.

⚖️ Part 4 — Trade-offs

A senior AI Engineer should also discuss trade-offs.

Larger Context

✅ More information available

❌ Higher token cost

❌ Higher latency

❌ More irrelevant information

❌ Still finite

Retrieval

✅ Lower context size

✅ Lower cost

✅ Better relevance

❌ Retrieval can miss required information

Semantic Search

✅ Finds conceptual relationships

❌ May miss exact identifiers

Lexical Search

✅ Excellent for exact symbols

❌ Poor semantic understanding

Code Graph

✅ Understands relationships

❌ More complex to build and maintain

Hierarchical Summaries

✅ Reduces context

❌ Summaries can lose important details

🎤 Follow-Up Interview Questions

After giving this answer, an interviewer could ask:

### 1. ❓ Why isn't semantic search alone sufficient?

💡 Answer: Because coding tasks frequently involve exact identifiers, class names, function names, error messages, and configuration keys. Lexical/symbol search handles these cases better.

### 2. ❓ Why isn't lexical search enough?

💡 Answer: Because developers often describe functionality using different terminology from the implementation. Semantic search helps retrieve conceptually related code.

### 3. ❓ How do you keep the index current?

💡 Answer: Use Git/CI change detection and incrementally update affected AST nodes, embeddings, dependency relationships, and summaries.

### 4. ❓ What if retrieving one file isn't enough?

💡 Answer: Use dependency-aware iterative retrieval to follow imports, callers, callees, interfaces, implementations, and relevant tests.

### 5. ❓ How do you know retrieval is good?

💡 Answer: Build a retrieval evaluation dataset and measure metrics such as Recall@K, Precision@K, MRR, and context-level precision/recall.

🛠️ Part 5 — Practical Project

🚀 Topic 01 – LLM Basics

 Interview question serios with my enhanded solution Project Structure
 practical project:
 stru ↓
🤖 Answer
🏆 Final Interview Answer

If I were answering the Tech Mahindra question in an interview, I would say:

I would not try to fit a 20-million-line repository into the model's context window. I would treat the repository as an indexed knowledge source and build a repository-understanding layer around the LLM.

First, I would parse the code structurally to create symbol and dependency information. Then I would combine lexical and semantic retrieval, because exact symbol matching and conceptual search solve different problems. I would maintain hierarchical summaries at repository, module, file, class, and function levels.

At runtime, the coding agent would start with a small context and iteratively retrieve additional files, symbols, dependencies, and tests as required. Finally, I would use incremental indexing driven by repository changes so only affected code is reprocessed.

I would also evaluate the retrieval layer independently using metrics such as Recall@K and MRR, because poor retrieval can cause an otherwise capable LLM to produce an incorrect answer.

So the fundamental solution isn't simply a larger context window. It is a combination of structured code indexing, hybrid retrieval, dependency-aware navigation, hierarchical summarization, iterative context construction, and incremental indexing.


🎯 Final Point — Tech Mahindra Interview Solution

💡 The Tech Mahindra interview solution is good because it correctly identifies the major architectural principles needed for repository-scale understanding:

🔍 Retrieve, don't stuff — don't put the entire repository into the LLM context.
🕸️ Index code structurally — understand symbols, references, and dependencies.
🔎🧠 Combine lexical + semantic search — exact matching and meaning-based retrieval complement each other.
📝 Use hierarchical summaries — navigate from repository/module/file level down to specific code.
🔄 Expand context iteratively — retrieve more information only when the agent needs it.
⚡ Incrementally update the index — don't rebuild a 20M-line repository index for every change.

💡 What is it good at?

✅ It gives a strong WHAT and WHY at the architecture level.

✅ It correctly recognizes that:

20M lines of code
        ↓
❌ Don't put everything into context
        ↓
✅ Build a repository understanding layer
        ↓
🔍 Retrieval + Code Structure + Search + Summaries
        ↓
🔄 Iterative Context
        ↓
🤖 LLM

⚠️ But what is it missing?

⚠️ The answer is high-level. It doesn't specify enough of the HOW.

For example:

"Index code by structure"

Good principle, but:

    🧩 How do we parse the code?
    🔷 How do we extract symbols?
    🕸️ How do we build the dependency graph?
    🗄️ Where do we store it?

Or:

"Combine semantic and lexical search"

Good principle, but:

    🔎 Which lexical search?
    🧠 Which embedding approach?
    ⚖️ How do we combine results?
    📊 How do we rank them?
    🚫 How do we prevent irrelevant code from entering context?

Or:

"Expand context iteratively"

Good principle, but:

    👤 Who decides what to retrieve next?
    📁 How does the agent know it needs another file?
    ⚠️ How do we prevent excessive retrieval?
    ⏱️ How do we control token cost and latency?

🧠 Therefore, our conclusion should be:

    ✅ The Tech Mahindra solution is architecturally strong and correctly identifies the core principles for repository-scale understanding, but it remains high-level. It explains what the system should do and why, while leaving the implementation details, technology choices, retrieval strategy, evaluation, scalability, and engineering trade-offs open for further design.

That's the distinction I recommend we document in the repository.

💼 Tech Mahindra Interview Solution
        ↓
✅ Strong architectural principles
        ↓
❓ Implementation details not specified
        ↓
🧠 Our Engineering Deep Dive
        ↓
🏗️ Concrete architecture
        ↓
🛠️ Working Repository Understanding Agent
