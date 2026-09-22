from fastapi.testclient import TestClient

from fast import app
from models.shopping_item import database


client = TestClient(app)


def setup_function() -> None:
    database.reset()


def test_crud_shopping_items() -> None:
    response = client.get("/items")
    assert response.status_code == 200
    assert len(response.json()) == 2

    response = client.post(
        "/items",
        json={"name": "Huevos", "quantity": 12, "purchased": False},
    )
    assert response.status_code == 201
    created_item = response.json()
    assert created_item == {
        "name": "Huevos",
        "quantity": 12,
        "purchased": False,
        "id": 3,
    }

    response = client.put(
        "/items/3",
        json={"name": "Huevos", "quantity": 6, "purchased": True},
    )
    assert response.status_code == 200
    assert response.json()["quantity"] == 6
    assert response.json()["purchased"] is True

    response = client.delete("/items/3")
    assert response.status_code == 204
    assert client.get("/items/3").status_code == 404


def test_rejects_invalid_quantity() -> None:
    response = client.post("/items", json={"name": "Arroz", "quantity": 0})
    assert response.status_code == 422


def test_returns_404_for_unknown_item() -> None:
    assert client.get("/items/999").status_code == 404
    assert client.put("/items/999", json={"name": "Cafe"}).status_code == 404
    assert client.delete("/items/999").status_code == 404