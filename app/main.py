from fastapi import FastAPI
from pydantic import BaseModel

from app.rag import load_manual_text, chunk_text, build_vectorstore, retrieve_context
from app.prompts import build_prompt
from app.llm_groq import query_groq
API_KEY = "YOUR_API_KEY"

app = FastAPI(title="Industrial RAG Assistant")

# ---------- Load once at startup ----------
text = load_manual_text("DIR_to_Dataset")
chunks = chunk_text(text)
vectorstore = build_vectorstore(chunks)

@app.get("/")

def root():
    return {"status" : "industrial assistant"}

@app.get("/square/{x}")
def square(x: int):
    return {"result": x * x}

@app.get("/multiply")
def multiple(a : int, b : int):
    return{"result" : a*b}


# ---------- Request schema ----------
class QuestionRequest(BaseModel):
    question: str


# ---------- API Endpoint ----------
@app.post("/ask")
def ask_question(req: QuestionRequest):
    context = retrieve_context(vectorstore, req.question)
    prompt = build_prompt(context, req.question)
    answer = query_groq(API_KEY, prompt)

    return {
        "question": req.question,
        "answer": answer
    }


