import requests
import pytest
from jsonschema import validate

HOST = "https://reqres.in"
get_user_schema = {
    "type": "object",
    "properties": {
        "data": {
            "type": "object",
            "properties": {
                "id": {"type": "number"},
                "email": {"type": "string"},
                "first_name": {"type": "string"},
            },
            "required": ["id", "first_name"]
        },
    },
    "required": ["data"]
}
positive_id = [1, 2, 3]
negative_id = [-2147483648, -2147483647, -1, 0, 100, 2147483647, 2147483648]


@pytest.mark.parametrize("id", positive_id)
def test_positive_get_user(id):
    response = requests.get(f"{HOST}/api/users/{id}")
    assert response.status_code == 200
    validate(instance=response.json(), schema=get_user_schema)


@pytest.mark.parametrize("id", negative_id)
def test_negative_get_user(id):
    response = requests.get(f"{HOST}/api/users/{id}")
    assert response.status_code == 404
    # validate(instance=response.json(), schema=valid_user_schema)
    # на любые неправильные запросы приходит ответ с пустым телом, поэтому нет валидации ответа