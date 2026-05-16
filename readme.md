# SHL AI Assessment Recommendation System

An AI-powered conversational recommendation engine built for the SHL Research Intern – AI Application assignment.

This system helps recruiters and hiring teams discover relevant SHL assessments through natural language conversations using semantic retrieval, vector embeddings, FAISS similarity search, and conversational clarification workflows.

---

# Architecture + Tech Stack

```text
┌───────────────────────────────────────────────┐
│            Recruiter / HR User               │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│         Streamlit Conversational UI          │
│                                               │
│  Technology:                                  │
│  • Streamlit                                  │
│  • Python                                     │
│                                               │
│  Features:                                    │
│  • Recruiter-Friendly Chat Experience         │
│  • Multi-turn Conversations                   │
│  • Assessment Recommendations                 │
│  • Clickable SHL URLs                         │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│             FastAPI Backend API              │
│                                               │
│  Technology:                                  │
│  • FastAPI                                    │
│  • Python                                     │
│  • Swagger / OpenAPI                          │
│                                               │
│  Features:                                    │
│  • Conversational Routing                     │
│  • Clarification Questions                    │
│  • End-of-Conversation Detection              │
│  • Legal/Compliance Refusal Handling          │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│         Semantic Retrieval Engine             │
│                                               │
│  Technology:                                  │
│  • Sentence Transformers                      │
│  • FAISS                                      │
│  • NumPy                                      │
│                                               │
│  Features:                                    │
│  • Vector Embeddings                          │
│  • Semantic Similarity Search                 │
│  • Assessment Ranking                         │
│  • Retrieval-Augmented Workflow               │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│            SHL Assessment Catalog             │
│                                               │
│  Technology:                                  │
│  • JSON-based Data Storage                    │
│                                               │
│  Data Stored:                                 │
│  • Assessment Metadata                        │
│  • Test Types                                 │
│  • Product URLs                               │
└───────────────────────────────────────────────┘
```

---

# Features

- Conversational recruiter-style workflow
- Semantic search using vector embeddings
- FAISS vector similarity retrieval
- Multi-turn conversation support
- Clarification-based recommendation flow
- Assessment refinement support
- Legal/compliance refusal handling
- End-of-conversation detection
- Streamlit conversational frontend
- FastAPI backend API
- Swagger/OpenAPI documentation
- Retrieval-Augmented Generation (RAG)-style architecture

---

# Example Capabilities

The system can:

- Recommend assessments for technical hiring
- Suggest leadership and executive assessments
- Handle graduate hiring workflows
- Recommend contact center assessments
- Support healthcare/admin hiring scenarios
- Recommend industrial safety assessments
- Ask recruiter clarification questions
- Support iterative recommendation refinement
- Handle legal/compliance refusal scenarios

---

# Project Structure

```text
SHL-AI-Application/
│
├── app/
│   ├── main.py
│   └── retrieval.py
│
├── frontend/
│   └── streamlit_app.py
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
├── runtime.txt
└── README.md
```

---

# How It Works

## 1. Assessment Catalog

A curated SHL assessment catalog is stored in:

```text
catalog.json
```

Each assessment contains:
- assessment name
- description
- assessment type
- product URL

---

## 2. Embedding Generation

Assessment descriptions are converted into dense vector embeddings using:

```text
all-MiniLM-L6-v2
```

from Sentence Transformers.

---

## 3. FAISS Vector Indexing

Embeddings are stored inside a FAISS vector index for efficient semantic similarity retrieval.

---

## 4. Conversational Retrieval Workflow

When recruiters submit hiring requirements:

1. User query is embedded
2. Semantic similarity search is performed
3. Relevant assessments are retrieved
4. Clarification logic refines recommendations
5. Structured recommendations are returned

---

# Conversational Behaviors Implemented

## Clarification Questions

Examples:
- leadership seniority clarification
- language/accent clarification
- graduate hiring clarification
- healthcare bilingual clarification
- industrial safety clarification

---

## Refinement Support

Supports iterative refinement:
- add/remove assessments
- cognitive assessment refinement
- situational judgement refinement
- simulation-focused recommendations

---

## Legal/Compliance Refusal

The assistant avoids providing:
- legal advice
- regulatory interpretation
- compliance certification claims

---

## End-of-Conversation Detection

The system detects completion phrases such as:
- confirmed
- perfect
- thanks
- looks good

and marks:

```json
"end_of_conversation": true
```

---

# API Endpoints

## Root Endpoint

```http
GET /
```

Returns API health message.

---

## Health Check

```http
GET /health
```

Returns service status.

---

## Chat Recommendation Endpoint

```http
POST /chat
```

### Example Request

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

### Example Response

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

## 1. Clone Repository

```bash
git clone <repository-url>
cd SHL-AI-Application
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

### Activate

#### Windows

```bash
.\venv\Scripts\Activate.ps1
```

#### Linux/macOS

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Run FastAPI Backend

```bash
python -m uvicorn app.main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

Swagger Docs:

```text
http://127.0.0.1:8000/docs
```

---

## 5. Run Streamlit Frontend

```bash
python -m streamlit run frontend/streamlit_app.py
```

Frontend URL:

```text
http://localhost:8501
```

---

# Deployment

## Backend Deployment

Recommended:
- Render
- Railway
- Hugging Face Spaces

---

## Frontend Deployment

Recommended:
- Streamlit Cloud

---

# Future Improvements

- Hybrid BM25 + vector retrieval
- LLM-powered reasoning layer
- Dynamic catalog scraping
- Advanced reranking pipeline
- Persistent conversation memory
- Authentication and recruiter accounts
- Analytics dashboard
- Feedback-based ranking optimization

---

# Author

Purushotham S

Built as part of the SHL Research Intern – AI Application assignment.