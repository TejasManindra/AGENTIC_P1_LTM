from fastapi.testclient import TestClient

from backend.main import app


client = TestClient(app)


def test_analyze_endpoint():
    response = client.post(
        "/api/analyze",
        json={
            "query": "Which region generated the highest profit?"
        },
    )

    assert response.status_code == 200

    result = response.json()

    assert result["query"] == (
        "Which region generated the highest profit?"
    )

    assert result["sql"]

    assert result["analysis"]

    assert len(result["insights"]) == 2

    assert len(result["recommendations"]) == 2