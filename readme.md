# SHL AI Assessment Recommendation System

> AI-powered conversational recommendation engine for recommending SHL assessments using semantic retrieval, vector search, and conversational refinement workflows.

---

# Overview

This project was built as part of the **SHL Research Intern – AI Application Assignment**.

The system helps recruiters and hiring managers discover the most relevant SHL assessments using natural language conversations.

Instead of keyword matching, the system uses:

- Semantic Retrieval
- Vector Embeddings
- FAISS Similarity Search
- Conversational Recommendation Logic

to generate grounded assessment recommendations.

---

# Key Features

| Feature | Description |
|---|---|
| Conversational Recommendations | Supports natural language hiring queries |
| Semantic Search | Uses embeddings instead of keyword-only matching |
| RAG-style Retrieval | Retrieves grounded SHL catalog recommendations |
| FAISS Vector Search | Efficient similarity-based retrieval |
| Clarification Questions | Asks follow-up questions when requirements are ambiguous |
| Refinement Support | Supports iterative recommendation refinement |
| Legal Refusal Handling | Avoids giving legal/compliance advice |
| OpenAPI Documentation | Auto-generated Swagger API docs |
| FastAPI Backend | Production-ready Python API framework |

---

# System Architecture

```text
┌─────────────────────────────────────────────────────────┐
│                        USER QUERY                      │
│      Example: "Hiring senior Java backend engineer"   │
└───────────────────────┬─────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────┐
│                 FASTAPI BACKEND API                    │
│                                                         │
│  Tech Used:                                             │
│  - FastAPI                                              │
│  - Python                                               │
│  - Pydantic                                             │
│  - OpenAPI / Swagger                                    │
└───────────────────────┬─────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────┐
│              CONVERSATION LOGIC LAYER                  │
│                                                         │
│  Responsibilities:                                      │
│  - Clarification Questions                              │
│  - Recommendation Refinement                            │
│  - Legal Refusal Handling                               │
│  - End-of-Conversation Detection                        │
└───────────────────────┬─────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────┐
│           SENTENCE TRANSFORMER MODEL                   │
│                                                         │
│  Model Used:                                            │
│  - all-MiniLM-L6-v2                                     │
│                                                         │
│  Purpose:                                               │
│  - Convert queries into semantic embeddings             │
│  - Understand contextual meaning                        │
└───────────────────────┬─────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────┐
│                 FAISS VECTOR SEARCH                    │
│                                                         │
│  Tech Used:                                             │
│  - FAISS                                                │
│                                                         │
│  Purpose:                                               │
│  - Fast similarity search                               │
│  - Semantic retrieval                                   │
│  - Vector ranking                                       │
└───────────────────────┬─────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────┐
│              SHL ASSESSMENT CATALOG                    │
│                                                         │
│  Storage Used:                                          │
│  - JSON Catalog                                         │
│                                                         │
│  Contains:                                              │
│  - Assessment Name                                      │
│  - Description                                          │
│  - Assessment Type                                      │
│  - Product URL                                          │
└───────────────────────┬─────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────┐
│            STRUCTURED RECOMMENDATIONS                  │
│                                                         │
│  Output Includes:                                       │
│  - Relevant Assessments                                 │
│  - SHL Product URLs                                     │
│  - Test Types                                           │
│  - Conversational Response                              │
└─────────────────────────────────────────────────────────┘
```

---

# Tech Stack

| Layer | Technology Used |
|---|---|
| Backend Framework | FastAPI |
| API Documentation | Swagger / OpenAPI |
| Programming Language | Python |
| Embedding Model | Sentence Transformers |
| Semantic Model | all-MiniLM-L6-v2 |
| Vector Database | FAISS |
| Data Storage | JSON Catalog |
| AI Pattern | Retrieval-Augmented Generation (RAG) |
| Deployment Platform | Render |
| Package Management | pip + virtualenv |

---

# Project Structure

```text
shl-recommender/
│
├── app/
│   ├── main.py
│   └── retrieval.py
│
├── data/
│   ├── catalog.json
│   ├── embeddings.npy
│   └── faiss.index
│
├── scripts/
│   └── build_embeddings.py
│
├── requirements.txt
├── README.md
└── Procfile
```

---

# API Endpoints

| Endpoint | Method | Purpose |
|---|---|---|
| `/` | GET | Root API status |
| `/health` | GET | Health check |
| `/chat` | POST | Conversational recommendations |

---

# Example Request

```json
{
  "messages": [
    {
      "role": "user",
      "content": "Hiring senior Java backend engineer"
    }
  ]
}
```

---

# Example Response

```json
{
  "reply": "Found 5 relevant assessments based on the role requirements.",
  "recommendations": [
    {
      "name": "Core Java (Advanced Level) (New)",
      "url": "https://www.shl.com/products/product-catalog/view/core-java-advanced-level-new/",
      "test_type": "K"
    }
  ],
  "end_of_conversation": false
}
```

---

# Installation

## Clone Repository

```bash
git clone <your-repo-url>
cd shl-recommender
```

## Create Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
.\venv\Scripts\Activate.ps1
```

### Linux/macOS

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Build Embeddings

```bash
python scripts/build_embeddings.py
```

## Run Server

```bash
python -m uvicorn app.main:app
```

---

# Swagger API Documentation

```text
http://127.0.0.1:8000/docs
```

---

# Deployment

Deployment-ready for:
- Render
- Railway
- Hugging Face Spaces
- Docker-compatible cloud platforms

---

# Future Improvements

- Multi-turn conversational memory
- Hybrid BM25 + vector retrieval
- Frontend chat interface
- LLM-powered reasoning layer
- Dynamic catalog scraping
- Reranking pipelines

---

# Author

Purushotham S

Built for the SHL Research Intern – AI Application Assignment.