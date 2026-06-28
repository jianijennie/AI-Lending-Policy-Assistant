# Week 2 Sprint Plan

## Sprint Goal

Build the first functional version of the AI knowledge base by transforming structured policy chunks into searchable vector embeddings.

---

# Team Responsibilities

| Member             | Role                             | Tasks                                                                                                                                                                                                    | Deliverables                                                                   |
| ------------------ | -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| **Maksim**         | Finance & Policy Analyst         | Enhance all policy chunks with structured metadata, develop the benchmark Question Bank, and create the Ground Truth dataset for evaluation.                                                             | `Metadata.csv`<br>`QuestionBank.xlsx`<br>`GroundTruth.xlsx`                    |
| **Jiani**          | UX, Compliance & Quality Analyst | Design the user interface in Figma, including the chat interface, document upload page, knowledge base dashboard, and user workflow. Review compliance requirements and improve overall user experience. | UI Wireframes<br>User Flow Diagram<br>Figma Prototype                          |
| **Sameep**         | AI / RAG & Data Engineer         | Generate embeddings for all document chunks, build the ChromaDB vector database, perform Top-K retrieval testing, and validate retrieval accuracy.                                                       | Initial RAG Knowledge Base<br>ChromaDB Setup<br>Retrieval Test Results         |
| **Samyak & Umair** | Full-Stack / Platform Engineers  | Initialize the Next.js frontend and Node.js + TypeScript backend, build core API endpoints, and integrate the backend with the AI retrieval pipeline.                                                    | Frontend & Backend Project Framework<br>REST API<br>Initial System Integration |

---

# Sprint Milestones

* [ ] Finalise metadata for all policy chunks
* [ ] Generate embeddings using `text-embedding-3-large`
* [ ] Import embeddings into ChromaDB
* [ ] Verify Top-K semantic retrieval accuracy
* [ ] Initialise the frontend and backend architecture
* [ ] Prepare the project for GPT-4o integration in Week 3

---

# Week 2 Deliverables

| Category              | Deliverable                   |
| --------------------- | ----------------------------- |
| Knowledge Engineering | Structured Metadata           |
| AI / RAG              | OpenAI Embeddings             |
| Vector Database       | ChromaDB Collection           |
| Retrieval Testing     | Top-K Evaluation Results      |
| Backend               | Node.js + TypeScript API      |
| Frontend              | Next.js Project Scaffold      |
| Integration           | Initial End-to-End Connection |

---

# 6-Week Project Roadmap

| Week                          | Sprint Goal                             | Key Deliverables                                    |
| ----------------------------- | --------------------------------------- | --------------------------------------------------- |
| **Week 1**                    | Policy Analysis & Knowledge Structuring | Taxonomy, Chunking, Initial Repository              |
| **Week 2** *(Current Sprint)* | Build the Knowledge Base                | Metadata, Embeddings, ChromaDB, Backend Setup       |
| **Week 3**                    | RAG Pipeline Development                | GPT-4o Integration, Retrieval Pipeline, API Testing |
| **Week 4**                    | Product Development                     | Next.js Frontend, Chat Interface, Source Citation   |
| **Week 5**                    | System Integration & Testing            | End-to-End Demo, Bug Fixes, Performance Testing     |
| **Week 6**                    | Final Presentation & Deployment         | Final Demo, Documentation, Presentation Slides      |

---

# Success Criteria

By the end of Week 2, the team should have:

* A structured metadata dataset for all policy chunks.
* Vector embeddings generated using OpenAI's `text-embedding-3-large` model.
* A fully functional ChromaDB knowledge base.
* Verified semantic retrieval through Top-K testing.
* A working backend API connected to the retrieval layer.
* A Next.js frontend project scaffold ready for GPT-4o integration in Week 3.

---

## Next Sprint Preview (Week 3)

Focus on integrating GPT-4o with the retrieval pipeline to build the first end-to-end Retrieval-Augmented Generation (RAG) chatbot prototype.
