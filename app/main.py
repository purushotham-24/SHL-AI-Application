from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from app.retrieval import search_assessments

app = FastAPI()


# -----------------------------
# Request Models
# -----------------------------
class Message(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    messages: List[Message]


# -----------------------------
# Root Endpoint
# -----------------------------
@app.get("/")
def root():
    return {
        "message": "SHL recommender API running"
    }


# -----------------------------
# Health Endpoint
# -----------------------------
@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


# -----------------------------
# Chat Endpoint
# -----------------------------
@app.post("/chat")
def chat(request: ChatRequest):

    # ------------------------------------------------
    # GET LATEST USER MESSAGE ONLY
    # ------------------------------------------------
    latest_message = ""

    for msg in reversed(request.messages):

        if msg.role == "user":

            latest_message = msg.content.lower()
            break

    # ------------------------------------------------
    # GREETING HANDLER
    # ------------------------------------------------
    greetings = [
        "hi",
        "hello",
        "hey",
        "good morning",
        "good evening"
    ]

    if latest_message.strip() in greetings:

        return {
            "reply": (
                "Hello! Please describe the hiring role "
                "or assessment requirements, and I will "
                "recommend relevant SHL assessments."
            ),
            "recommendations": None,
            "end_of_conversation": False
        }

    # ------------------------------------------------
    # RESET CONVERSATION
    # ------------------------------------------------
    reset_words = [
        "start over",
        "new hiring request",
        "reset"
    ]

    if any(word in latest_message for word in reset_words):

        return {
            "reply": (
                "Conversation reset successfully. "
                "Please describe the new hiring requirement."
            ),
            "recommendations": None,
            "end_of_conversation": False
        }

    # ------------------------------------------------
    # END OF CONVERSATION DETECTION
    # ------------------------------------------------
    end_words = [
        "confirmed",
        "perfect",
        "thanks",
        "thank you",
        "looks good",
        "final shortlist",
        "that works",
        "great"
    ]

    if any(word in latest_message for word in end_words):

        return {
            "reply": "Final shortlist confirmed.",
            "recommendations": None,
            "end_of_conversation": True
        }

    # ------------------------------------------------
    # LEGAL / COMPLIANCE REFUSAL
    # ------------------------------------------------
    legal_words = [
        "legal",
        "law",
        "compliance",
        "regulation",
        "hipaa",
        "mandatory"
    ]

    if any(word in latest_message for word in legal_words):

        return {
            "reply": (
                "I can help recommend assessments, "
                "but legal or compliance interpretation "
                "should be reviewed with your legal team."
            ),
            "recommendations": None,
            "end_of_conversation": False
        }

    # ------------------------------------------------
    # LEADERSHIP CLARIFICATION
    # ------------------------------------------------
    if (
        "leadership" in latest_message
        or "cxo" in latest_message
        or "director" in latest_message
    ):

        if (
            "15" not in latest_message
            and "senior" not in latest_message
        ):

            return {
                "reply": (
                    "Could you share the seniority level "
                    "or experience range for these "
                    "leadership candidates?"
                ),
                "recommendations": None,
                "end_of_conversation": False
            }

        # Improve leadership retrieval
        latest_message += (
            " leadership executive personality cognitive"
        )

    # ------------------------------------------------
    # CONTACT CENTER CLARIFICATION
    # ------------------------------------------------
    if (
        "contact center" in latest_message
        or "call center" in latest_message
        or "customer service" in latest_message
    ):

        if (
            "english" not in latest_message
            and "us" not in latest_message
            and "uk" not in latest_message
        ):

            return {
                "reply": (
                    "What language or accent will "
                    "the customer interactions use?"
                ),
                "recommendations": None,
                "end_of_conversation": False
            }

    # ------------------------------------------------
    # GRADUATE CLARIFICATION
    # ------------------------------------------------
    if (
        "graduate" in latest_message
        or "freshers" in latest_message
        or "entry level" in latest_message
    ):

        if (
            "cognitive" not in latest_message
            and "situational" not in latest_message
        ):

            return {
                "reply": (
                    "Would you like the recommendations "
                    "to include cognitive or situational "
                    "judgement assessments as well?"
                ),
                "recommendations": None,
                "end_of_conversation": False
            }

    # ------------------------------------------------
    # HEALTHCARE CLARIFICATION
    # ------------------------------------------------
    if (
        "healthcare" in latest_message
        or "medical" in latest_message
    ):

        if (
            "english" not in latest_message
            and "spanish" not in latest_message
            and "bilingual" not in latest_message
        ):

            return {
                "reply": (
                    "Are candidates expected to be "
                    "bilingual or English-only?"
                ),
                "recommendations": None,
                "end_of_conversation": False
            }

    # ------------------------------------------------
    # INDUSTRIAL / SAFETY CLARIFICATION
    # ------------------------------------------------
    if (
        "chemical" in latest_message
        or "plant operator" in latest_message
        or "safety" in latest_message
    ):

        if "industrial" not in latest_message:

            return {
                "reply": (
                    "Is this hiring requirement for "
                    "a general environment or an "
                    "industrial facility?"
                ),
                "recommendations": None,
                "end_of_conversation": False
            }

    # ------------------------------------------------
    # SEMANTIC RETRIEVAL
    # ------------------------------------------------
    recommendations = search_assessments(
        latest_message
    )

    # ------------------------------------------------
    # FINAL RESPONSE
    # ------------------------------------------------
    return {
        "reply": (
            f"Based on the hiring requirements, "
            f"I found {len(recommendations)} relevant "
            f"SHL assessments for evaluating "
            f"candidate fit."
        ),
        "recommendations": recommendations,
        "end_of_conversation": False
    }