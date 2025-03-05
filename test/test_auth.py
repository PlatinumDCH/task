from fastapi.testclient import TestClient
import pytest
from src.main import app



@pytest.mark.asyncio
async def test_register_user_correct( fastapi_testclient, testdatabase):
    register_data = {
        "email": "johndoe@example.com",
        "full_name": "John Doe",
        "name": "John",
        "password": "New123!"
    }

    response = fastapi_testclient.post('/auth/register/', json=register_data)
    response_data = response.json()
    
    assert response.status_code == 200
    assert response_data["email"] == register_data["email"]
    assert response_data["full_name"] == register_data["full_name"]
    assert response_data["name"] == register_data["name"]

@pytest.mark.asyncio
async def test_register_user_fail( fastapi_testclient):
    register_data = {
        "email": "johndoe@example.com",
        "full_name": "John Doe",
        "name": "John",
        "password": "1"
    }

    response = fastapi_testclient.post('/auth/register/', json=register_data)
    assert response.status_code == 422

@pytest.mark.asyncio
async def test_login_user(
    fastapi_testclient,
    testdatabase
):
    register_data = {
        "email": "johndoe@example.com",
        "full_name": "John Doe",
        "name": "John",
        "password": "New123!"
    }
    response_register = fastapi_testclient.post('/auth/register/', json=register_data)
    assert response_register.status_code == 200
    login_data = {
        "username": "johndoe@example.com",
        "password": "New123!"
    }
    response_login = fastapi_testclient.post(
        '/auth/login', data=login_data
    )
    assert response_login.status_code == 200
