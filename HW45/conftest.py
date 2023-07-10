import pytest

from HW45.classes import HTTPClient


@pytest.fixture()
def client():
    client = HTTPClient()
    yield client
    client.delete_user()
