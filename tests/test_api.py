import pytest
import requests

BASE_URL = "http://localhost:5001"

API_KEY_VALID = "valid_api_key"
API_KEY_INVALID = "invalid_api_key"

def test_auth_success():
    headers = {"Authorization": API_KEY_VALID}
    response = requests.get(f"{BASE_URL}/auth", headers=headers)
    assert response.status_code == 200
    assert "Autenticación exitosa" in response.json()["message"]

def test_auth_failure():
    headers = {"Authorization": API_KEY_INVALID}
    response = requests.get(f"{BASE_URL}/auth", headers=headers)
    assert response.status_code == 403

def test_service_without_auth():
    response = requests.post(f"http://localhost:5002/service", json={"inputs": ["A", "B"]})
    assert response.status_code == 403
