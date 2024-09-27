from fastapi import FastAPI
import re
import requests

app = FastAPI()

@app.get("/ask")
def ask_question(question: str):
    cleaned_question = clean_question(question)
    response = send_to_datascience_endpoint(cleaned_question)
    return {"answer": response}

def clean_question(question: str) -> str:
    question = question.lower()
    question = re.sub(r'[^a-zA-Z0-9\s]', '', question)
    return question

def send_to_datascience_endpoint(cleaned_question: str) -> str:
    # Mock sending the cleaned question to a data science endpoint
    endpoint_url = "http://datascience-team-endpoint.com/api"
    payload = {"question": cleaned_question}
    
    try:
        response = requests.post(endpoint_url, json=payload)
        response.raise_for_status()
        return response.json().get("answer", "Sorry, I couldn't find an answer to your question.")
    except requests.exceptions.RequestException as e:
        print(f"Error sending request to data science endpoint: {e}")
        return "Sorry, I couldn't process your question at the moment."

