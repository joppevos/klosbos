import requests


def call_fastapi(question):
    url = "http://127.0.0.1:8000/ask"
    params = {"question": question}
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error calling FastAPI endpoint: {e}")
        return None


if __name__ == "__main__":
    question = "I want to travel to Turkey"
    response = call_fastapi(question)
    if response:
        print(f"Response from FastAPI: {response}")
