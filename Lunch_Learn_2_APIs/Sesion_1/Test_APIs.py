import requests

response = requests.post(
    "http://127.0.0.1:5000/summarize",
    json={
        "text": "Tell me about Slalom Consulting"
    }
)

print(response.status_code)
print(response.json())