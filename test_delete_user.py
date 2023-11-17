import requests
import pytest
from jsonschema import validate

HOST = "https://reqres.in"
id = [1, 2, 3]
negative_id = ["#", -1, 0, -2343593485938459845645645,
               "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffv"]


@pytest.mark.parametrize("id", id)
def test_positive_delete_users(id):
    response = requests.delete(f"{HOST}/api/users/{id}")
    assert response.status_code == 204


@pytest.mark.parametrize("id", negative_id)
def test_negative_get_users(id):
    response = requests.delete(f"{HOST}/api/users")
    assert response.status_code == 204
