# 🤖 AI Lending Policy Assistant

> **AI-powered Retrieval-Augmented Generation (RAG) platform for Mortgage & Asset Finance Brokers**

Search • Compare • Recommend • Cite

---

## 📖 Project Overview

The **AI Lending Policy Assistant** is an intelligent decision-support platform designed to help mortgage and asset finance brokers quickly search, compare, and understand lender policies using Large Language Models (LLMs) and Retrieval-Augmented Generation (RAG).

Instead of manually reading hundreds of pages of policy documents, brokers can ask natural language questions and instantly receive accurate answers with policy citations.

---

## 🎯 Problem Statement

### Current Workflow

```text
Broker
    │
    ▼
Open PDF
    │
Ctrl + F
    │
Read 100+ pages
    │
Compare multiple lenders manually
    │
Time-consuming & error-prone
```

### Our Solution

```text
Broker
    │
Ask Question
    │
AI retrieves relevant policies
    │
Compares multiple lenders
    │
Returns answer with source citation
```

---

# ✨ Key Features

- 📄 Upload lender policy documents (PDF)
- 🤖 AI-powered policy search
- 🔍 Semantic Retrieval (RAG)
- 📚 Source Citation
- 📊 Cross-Lender Comparison
- 🧠 Unified Lending Taxonomy
- 🏦 Broker Decision Support
- 👨‍💼 Human Review Workflow

---

# 🏗️ System Architecture

```text
                       Broker

                         │

                  Ask Question

                         │

               Next.js Frontend

                         │

                Backend API Server

                 (Node.js + TS)

                         │

        ┌────────────────┴────────────────┐

        │                                 │

 OpenAI Embedding API              OpenAI GPT-4o

        │                                 ▲

        ▼                                 │

      ChromaDB ───── Retrieve Chunks ─────┘

        │

 Policy Documents (PDF)

        │

 Chunking + Metadata
```

---

# 🛠 Technology Stack

| Layer | Technology |
|---------|------------|
| Frontend | Next.js |
| Backend | Node.js + TypeScript |
| LLM | GPT-4o |
| Embedding Model | text-embedding-3-large |
| Vector Database | ChromaDB |
| Relational Database | PostgreSQL |
| Language | TypeScript |
| AI Framework | OpenAI API |

---

# 📂 Repository Structure

```text
AI-Lending-Policy-Assistant/

│
├── README.md
│
├── docs/
│   ├── Taxonomy.md
│   ├── Architecture.md
│   ├── QuestionBank.md
│   ├── GroundTruth.md
│   ├── ProjectRoadmap.md
│   └── MeetingNotes.md
│
├── policies/
│   ├── Resimac/
│   ├── Pepper/
│   ├── Liberty/
│   └── Latitude/
│
├── frontend/
│
├── backend/
│
├── database/
│
├── assets/
│
└── presentation/
```

---

# 📚 Knowledge Base

Our RAG knowledge base is built upon a unified taxonomy rather than individual lender document structures.

```text
Borrower

├── Residency

├── Citizenship

├── Employment

└── Business

        │

        ├── ABN

        ├── GST

        ├── Trading History

        └── Industry

Loan

├── Amount

├── Term

├── Balloon

└── LVR

Asset

├── Vehicle

├── Equipment

├── Machinery

└── Software
```

---

# 🔄 RAG Pipeline

```text
Upload PDF

↓

Extract Text

↓

Chunking

↓

Metadata Tagging

↓

Embedding

↓

ChromaDB

↓

Semantic Retrieval

↓

GPT-4o

↓

Answer with Citation
```

---

# 📊 Development Roadmap

| Week | Progress |
|------|----------|
| Week 1 | ✅ Policy Classification |
| Week 1 | ✅ Taxonomy Design |
| Week 2 | ✅ Chunking |
| Week 2 | ⏳ Metadata Design |
| Week 3 | ⏳ Embedding |
| Week 3 | ⏳ ChromaDB |
| Week 4 | ⏳ GPT Integration |
| Week 5 | ⏳ Frontend Development |
| Week 6 | ⏳ Testing & Presentation |

---

# 📈 Current Progress

```text
██░░░░░░░░░░░░░░

20%
```

### Completed

- Policy Classification

- Chunking

- Taxonomy

### In Progress

- Metadata Design

### Coming Soon

- Embedding

- ChromaDB

- GPT-4o

- Frontend

---

# 💡 Example Questions

```text
Can a sole trader with a 2-year ABN qualify?

Which lender has the lowest minimum GST requirement?

Can software be financed?

Compare ABN requirements across all lenders.

Which lender is most suitable for this client?

Explain why Pepper is recommended.
```

---

# 📸 Demo

> 🚧 Screenshots will be added after the frontend is completed.

```
Chat Interface

────────────────────────────

Question

Can software be financed?

────────────────────────────

Answer

No.

Software is excluded under Pepper Asset Finance Policy.

Source

Pepper Policy

Page 28
```

---

# 📑 Documentation

| Document | Description |
|-----------|-------------|
| Taxonomy | Unified Lending Policy Taxonomy |
| Architecture | System Design |
| Question Bank | Benchmark Questions |
| Ground Truth | Expected Answers |
| Roadmap | Weekly Development Plan |

---

# 🎯 Future Improvements

- Multi-Lender Recommendation Engine
- Policy Difference Analysis
- Knowledge Graph Integration
- OCR Support
- User Authentication
- Policy Version Management
- Automatic Policy Updates
- Broker Dashboard

---

# 👥 Team

| Role | Responsibility |
|------|----------------|
| Business | Policy Analysis, Taxonomy, Metadata |
| IT | Backend, Frontend, AI Integration |

---

# 📄 License

This project is developed for educational and research purposes.

© 2026 AI Lending Policy Assistant Team
