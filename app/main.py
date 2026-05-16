from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

from app.retrieval import search_assessments

app = FastAPI()


class Message(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    messages: List[Message]


@app.get("/")
def root():
    return {"message": "SHL recommender API running"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/chat")
def chat(request: ChatRequest):

    latest_message = request.messages[-1].content.lower()

    # End conversation
    if any(word in latest_message for word in [
        "thanks",
        "thank you",
        "perfect",
        "confirmed",
        "that works",
        "that's good"
    ]):

        return {
            "reply": "Glad I could help. Final shortlist confirmed.",
            "recommendations": [],
            "end_of_conversation": True
        }

    # Legal refusal
    if any(word in latest_message for word in [
        "legal",
        "law",
        "compliance",
        "regulation"
    ]):

        return {
            "reply": "I can help recommend assessments, but I cannot provide legal or regulatory advice.",
            "recommendations": [],
            "end_of_conversation": False
        }

    # Clarification logic
    if "developer" in latest_message and "senior" not in latest_message:

        return {
            "reply": "What seniority level is the role? Junior, mid-level, or senior?",
            "recommendations": [],
            "end_of_conversation": False
        }

    if "contact centre" in latest_message or "contact center" in latest_message:

        return {
            "reply": "What language are the calls in?",
            "recommendations": [],
            "end_of_conversation": False
        }

    # Refinement logic
    if "personality" in latest_message:
        results = search_assessments("personality leadership behavior opq")

    elif "cognitive" in latest_message:
        results = search_assessments("cognitive aptitude reasoning verify")

    elif "excel" in latest_message:
        results = search_assessments("excel microsoft office")

    elif "word" in latest_message:
        results = search_assessments("microsoft word office")

    elif "safety" in latest_message:
        results = search_assessments("safety dependability industrial")

    elif "java" in latest_message:
        results = search_assessments("java spring sql backend engineer")

    else:
        results = search_assessments(latest_message)

    recommendations = []

    for item in results:
        recommendations.append({
            "name": item["name"],
            "url": item["url"],
            "test_type": item["test_type"]
        })

    return {
        "reply": f"Found {len(recommendations)} relevant assessments based on the role requirements.",
        "recommendations": recommendations,
        "end_of_conversation": False
    }