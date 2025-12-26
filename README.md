# 🏭 Industrial RAG Assistant

A Retrieval-Augmented Generation (RAG) based industrial assistant designed for manufacturing environments.

This system helps operators and engineers troubleshoot machine errors by retrieving relevant documentation and generating safe, concise answers using an LLM.

---

## 🚀 Features
- Semantic retrieval using FAISS and local embeddings
- Safety-aware prompt engineering
- Real-time answer generation using Groq (LLaMA 3.1)
- REST API built with FastAPI
- Modular and model-agnostic architecture

---

## 🧠 Architecture Overview

User Query → Retrieval (FAISS) → Prompt Construction → LLM (Groq) → JSON Response

---

## 🗂 Project Structure

app/
├── main.py # FastAPI app
├── rag.py # Retrieval pipeline
├── prompts.py # Prompt templates
└── llm_groq.py # Groq LLM wrapper
data/
└── manuals.txt # Industrial documentation



---

## 🛠 Installation and Example

bash
pip install -r requirements.txt


------------------------------------

## Run the Application : 
uvicorn app.main:app --reload


Open Swagger UI at:
http://127.0.0.1:8000/docs


Example API Call:
{
  "question": "What should I do if error E101 occurs?"
}

Response:
{
  "question": "...",
  "answer": "..."
}
##
---------------------------------------------
USECASE:
Designed for R&D and manufacturing environments where safety, clarity, and reliability are critical.
