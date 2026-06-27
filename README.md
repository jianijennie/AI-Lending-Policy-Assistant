<p align="center">

# 🤖 AI Lending Policy Assistant

### AI-powered Decision Support Platform for Mortgage & Asset Finance Brokers

Search • Compare • Recommend • Cite

---

An intelligent Retrieval-Augmented Generation (RAG) platform that transforms lender policy documents into an AI-powered knowledge base, enabling brokers to instantly retrieve, compare and understand lending policies with trusted source citations.

</p>
# Table of Contents

- Overview
- Features
- Why This Project?
- Architecture
- Technology Stack
- Repository Structure
- Knowledge Base
- RAG Pipeline
- Demo
- Roadmap
- Documentation
- Team
- # Why This Project?

Mortgage and asset finance brokers often need to review hundreds of pages of lender policy documents before recommending suitable lending solutions.

Traditional workflows rely heavily on manual document searching and policy interpretation, which are both time-consuming and prone to human error.

Our platform applies Retrieval-Augmented Generation (RAG) to transform lender policy documents into an intelligent knowledge base that enables brokers to retrieve policy information within seconds while maintaining full source transparency.
# Product Vision

We aim to build an AI-powered policy assistant that not only answers policy questions but also provides lender comparisons, recommendation support, and explainable decision-making for finance professionals.
                         Broker

                           │

                     Ask Question

                           │

────────────────────────────────────────────

                    Frontend

                     Next.js

────────────────────────────────────────────

                     Backend

               Node.js + TypeScript

────────────────────────────────────────────

      Retrieval Pipeline

 ┌────────────────────────────────────────┐

 PDF

↓

Chunk

↓

Metadata

↓

Embedding

↓

ChromaDB

↓

Top-K Retrieval

↓

GPT-4o

↓

Answer + Citation

└────────────────────────────────────────┘

────────────────────────────────────────────

            PostgreSQL

Conversation History

Users

Logs

Feedback
