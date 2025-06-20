import pytest
from core import create_app

app = create_app()

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

def test_get_contact(client):
    res = client.get("/api/contact")
    assert res.status_code == 200
    assert "email" in res.json
    assert "name" in res.json

def test_get_skills(client):
    res = client.get("/api/skills")
    assert res.status_code == 200
    assert "highlights" in res.json
    assert "technical" in res.json
    assert isinstance(res.json["technical"], list)

def test_get_languages(client):
    res = client.get("/api/languages")
    assert res.status_code == 200
    assert isinstance(res.json, list)
    assert "Greek" in res.json

def test_get_experience(client):
    res = client.get("/api/experience")
    assert res.status_code == 200
    assert isinstance(res.json, list)

def test_get_education(client):
    res = client.get("/api/education")
    assert res.status_code == 200
    assert isinstance(res.json, dict)

def test_get_interests(client):
    res = client.get("/api/interests")
    assert res.status_code == 200
    assert isinstance(res.json, list)
    assert "Hiking" in res.json

def test_get_full_cv(client):
    res = client.get("/api/cv")
    assert res.status_code == 200
    assert "contact" in res.json
    assert "skills" in res.json
    assert "experience" in res.json
    assert "education" in res.json
    assert "languages" in res.json
    assert "interests" in res.json
