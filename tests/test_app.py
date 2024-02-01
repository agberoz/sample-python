import json
import pytest
from flask import Flask
from app.main import app



@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_code_smell(client):
    response = client.get('/code-smell')
    data = json.loads(response.data.decode('utf-8'))
    assert response.status_code == 200
    assert data['A'] == 10


def test_code_smell_again(client):
    response = client.get('/code-smell/again')
    data = json.loads(response.data.decode('utf-8'))
    assert response.status_code == 200
    assert data['reult'] == 100  # Assuming the condition c > 1 is true
    
def test_security(client):
    response = client.get('/security')
    assert response.status_code == 200


def test_calculate(client):
    response = client.get('/sum')
    assert response.status_code == 200
    
def test_calculate_dif(client):
    response = client.get('/dif')
    assert response.status_code == 200