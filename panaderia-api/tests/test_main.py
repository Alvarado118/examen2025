from fastapi.testclient import TestClient
from app.main import app
import pytest

client = TestClient(app)

def test_create_producto():
    response = client.post(
        "/api/v1/productos/",
        json={
            "nombre": "Pan Frances",
            "sku": "PAN-0001",
            "categoria": "Pan",
            "precio_unitario": 1.25,
            "stock": 120
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["nombre"] == "Pan Frances"
    assert data["sku"] == "PAN-0001"

def test_read_productos():
    response = client.get("/api/v1/productos/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_read_producto():
    response = client.get("/api/v1/productos/1")
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert "nombre" in data

def test_update_producto():
    response = client.put(
        "/api/v1/productos/1",
        json={
            "nombre": "Pan Frances Actualizado",
            "sku": "PAN-0001",
            "categoria": "Pan",
            "precio_unitario": 1.50,
            "stock": 100
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["nombre"] == "Pan Frances Actualizado"

def test_delete_producto():
    response = client.delete("/api/v1/productos/1")
    assert response.status_code == 200
    assert response.json()["message"] == "Producto eliminado"
