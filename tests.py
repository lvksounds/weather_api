import pytest
from fastapi.testclient import TestClient
from main import app
from app.infra.db_connection import get_database
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from app.models.predictions import Base

SQLALCHEMY_DATABASE_URL = "sqlite:///./app.db" # usando mesmo banco da produção

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

# Configuração do TestClient
client = TestClient(app)
@pytest.fixture
def client():
    return TestClient(app)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_database] = override_get_db

#como nao estou usando um banco de teste, comentado pra nao criar muitos registros a toa
def test_create_prediction(client):
    response = client.post("/predictions/", params={"city": "Itapemirim"})
    assert response.status_code == 201
    assert "detail" in response.json()
    assert response.json()["detail"] == "Previsão criada com sucesso."

def test_create_prediction_not_found(client):
    response = client.post("/predictions/", params={"city": "aaooossiiejjs"})
    assert response.status_code == 404
    assert "detail" in response.json()
    assert response.json()["detail"] == "Cidade não encontrada"

def test_get_all_predictions(client):
    response = client.get("/predictions/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Verifica se a resposta é uma lista

def test_get_prediction_by_city_and_date(client):
    response = client.get("/predictions/filter", params={"city": "Itapemirim", "date": "26/03/2025"})
    assert response.status_code == 200
    assert "city" in response.json()
    assert response.json()["city"] == "itapemirim"

def test_get_prediction_by_city_and_date_not_found(client):
    response = client.get("/predictions/filter", params={"city": "Paty do Alferes", "date": "26/03/2025"})
    assert response.status_code == 404
    assert response.json()["detail"] == "Previsão não encontrada."

def test_get_prediction_by_city_and_date_missing_city(client):
    response = client.get("/predictions/filter", params={"date": "25/03/2025"})
    assert response.status_code == 401
    assert response.json()["detail"] == "Cidade não informada."

def test_get_prediction_by_city_and_date_missing_date(client):
    response = client.get("/predictions/filter", params={"city": "Itapemirim"})
    assert response.status_code == 401
    assert response.json()["detail"] == "Data não informada."

#mudar sempre o id
def test_delete_prediction(client):
    response = client.delete("/predictions/delete/9")
    assert response.status_code == 200
    assert response.json()["detail"] == "Previsão deletada com sucesso"

def test_delete_prediction_not_found(client):
    response = client.delete("/predictions/delete/9")
    assert response.status_code == 404
    assert response.json()["detail"] == "Previsão não encontrada."
