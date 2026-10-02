from fastapi.testclient import TestClient
from unittest.mock import patch

from ejemplo_1 import app

client = TestClient(app)

@patch("main.requests.post")

#Caso válido
def test_summarize_success(mock_post):

    mock_post.return_value.status_code = 200

    mock_post.return_value.json.return_value = {
        "response": "LATAM sales grew 15%"
    }

    response = client.post(
        "/summarize",
        json={
            "text": "LATAM sales increased by 15%"
        }
    )

    assert response.status_code == 200

    assert response.json() == {
        "summary": "LATAM sales grew 15%"
    }

#Caso inválido
def test_summarize_missing_text():

    response = client.post(
        "/summarize",
        json={}
    )

    assert response.status_code == 422

#Caso con clave incorrecta
def test_summarize_wrong_field():

    response = client.post(
        "/summarize",
        json={
            "texto": "Hola"
        }
    )

    assert response.status_code == 422