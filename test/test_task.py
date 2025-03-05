import pytest

@pytest.mark.asyncio
async def test_create_task( fastapi_testclient, testdatabase):
    """
    integration test, CRUD task
    """
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
    response_json = response_login.json()
    access_token = response_json.get('access_token')
    assert access_token is not None

    headers = {"Authorization": f"Bearer {access_token}"}

    task_data = {
        "title": "New Task",
        "description": "Test task description"
    }
    response_create_task = fastapi_testclient.post(
        "/task/add",
        json=task_data,
        headers=headers
    )
    assert response_create_task.status_code == 200

    response_get_tasks = fastapi_testclient.get(
        "/task/edit",
        headers=headers
    )
    assert response_get_tasks.status_code == 200

    response_get_task = fastapi_testclient.get(
        f"/task/edit/{1}",
        headers=headers
    )
    assert response_get_task.status_code == 200

    update_data = {
        "title": "New Task Update",
        "description": "Test task description update"
    }
    response_update_task = fastapi_testclient.put(
        f"/task/edit/{1}",
        json=update_data,
        headers=headers
    )
    assert response_update_task.status_code == 200

    response_delete_task = fastapi_testclient.delete(
        f"/task/delete/{1}",
        headers=headers
    )
    assert response_delete_task.status_code == 200


