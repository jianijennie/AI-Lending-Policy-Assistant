# Week 4 Sprint Plan

## Sprint Goal

Optimise the end-to-end RAG system by improving system performance, implementing an automated policy update workflow, enhancing product usability, and preparing the platform for final testing and demonstration.

---

# Team Responsibilities

| Member | Role | Tasks | Deliverables |
|--------|------|-------|--------------|
| **Maksim** | Finance & Evaluation Analyst | Review evaluation results, validate answer quality using the Question Bank and Ground Truth dataset, analyse retrieval performance, and summarise system evaluation findings. | Evaluation Summary Report, Performance Analysis |
| **Jiani** | Product & Documentation Analyst | Review the end-to-end user journey, design and document the automated policy update workflow, prepare system architecture and workflow diagrams, validate dashboard usability, and support project documentation for the final presentation. | Policy Update Workflow, System Architecture Diagram, Product Documentation, User Guide |
| **Sameep** | AI / RAG Engineer | Optimise retrieval performance, improve prompt engineering, implement the automated policy update pipeline, and support incremental knowledge base updates. | Optimised RAG Pipeline, Policy Update Pipeline, Updated Prompt Templates |
| **Samyak & Umair** | Full-Stack / Platform Engineers | Integrate the policy upload interface with the backend, connect the update pipeline to the existing dashboard, improve API reliability, and enhance system stability. | Upload Functionality, Backend Integration, Dashboard Enhancements |

---

# Sprint Milestones

- [ ] Optimise retrieval quality and prompt engineering
- [ ] Implement an automated policy update pipeline
- [ ] Enable document upload with automatic knowledge base updates
- [ ] Improve dashboard usability and document management
- [ ] Complete system documentation and workflow diagrams
- [ ] Prepare the platform for final testing and demonstration

---

# Key Deliverables

| Category | Deliverable |
|----------|-------------|
| AI Optimisation | Improved Retrieval & Prompt Performance |
| Knowledge Base | Automated Policy Update Pipeline |
| Product | Policy Upload Workflow |
| Documentation | System Architecture, User Guide, Workflow Diagrams |
| Evaluation | Final Performance Summary |
| Platform | Stable Dashboard & Upload Functionality |

---

# Automated Policy Update Workflow

```
Upload New Policy
        ↓
Validate Document
        ↓
Chunk Document
        ↓
Generate Metadata
        ↓
Generate Embeddings
        ↓
Update ChromaDB
        ↓
Knowledge Base Updated
```

This workflow enables efficient incremental updates by processing only newly uploaded or modified policy documents, eliminating the need to rebuild the entire knowledge base.

---

# Success Criteria

By the end of Week 4, the team should have:

- A stable and optimised end-to-end RAG system.
- An automated workflow for updating policy documents.
- Improved retrieval quality supported by evaluation results.
- Complete product documentation and system workflow diagrams.
- A platform ready for final testing, demonstration, and deployment.

---

# Next Sprint Preview (Week 5)

Focus on comprehensive system testing, bug fixing, documentation refinement, final presentation preparation, and deployment readiness.
