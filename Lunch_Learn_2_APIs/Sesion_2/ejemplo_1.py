from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()


class SummaryRequest(BaseModel):
    text: str


@app.post("/summarize")
def summarize(payload: SummaryRequest):

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": f"Resume: {payload.text}",
            "stream": False
        }
    )

    response.raise_for_status()

    return {
        "summary": response.json()["response"]
    }