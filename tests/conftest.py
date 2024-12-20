import pytest

from ..app import app


@pytest.fixure
def app():
    client = app.test_client()
    return client

@pytest.fixture
def test_get_users_status_code():
    response = client.get('/api/v1/users')
    assert response.status_code == 200
