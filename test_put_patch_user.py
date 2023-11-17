import requests
import pytest
from jsonschema import validate

HOST = "https://reqres.in"
update_user_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "job": {"type": "string"},
        "id": {"type": "string"},
        "updatedAt": {"type": "string"},
    },
    "required": ["updatedAt"]
}

positive_data = [{"name": "George", "job": "lead_testerrr"},
                 {"name": "Olga", "job": "load_testerrr"},
                 {"name": "Victor", "job": "fun_testerrr"},
                 ]
id = [1, 2]

negative_data = [{"name": "\n\n\n", "job": "\t\t\t\t"},
                 {
                     "name": "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffv",
                     "job": "12"},
                 {"go": 312, "id": 142, "name": "yo", "das": "dasdkfdfj!!32"},
                 {1: 2, 3: 5, 0: ""},
                 {}
                 ]
negative_id = ["#", -1, 0, -2343593485938459845645645,
               "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffv"]


@pytest.mark.parametrize("id", id)
@pytest.mark.parametrize("data", positive_data)
def test_positive_put_user(id, data):
    response = requests.put(f"{HOST}/api/users/{id}", data)
    assert response.status_code == 200
    validate(instance=response.json(), schema=update_user_schema)
    # здесь и ниже следовало бы добавить проверку на то, что юзер действительно обновился, но
    # при запросе получить всех юзеров GET api/users, сервер выдает всегда один и тот же список
    # хотя и наотправлял новых через POST и наобновлял через PUT|PATCH
    # вероятно, что стоит заглушка. Поэтому такой проверки нет

@pytest.mark.parametrize("id", id)
@pytest.mark.parametrize("data", positive_data)
def test_positive_patch_user(id, data):
    response = requests.patch(f"{HOST}/api/users/{id}", data)
    assert response.status_code == 200
    validate(instance=response.json(), schema=update_user_schema)


@pytest.mark.parametrize("id", negative_id)
@pytest.mark.parametrize("data", negative_data)
def test_negative_put_user(id, data):
    response = requests.put(f"{HOST}/api/users/", data)
    assert response.status_code == 200
    validate(instance=response.json(), schema=update_user_schema)


@pytest.mark.parametrize("id", negative_id)
@pytest.mark.parametrize("data", negative_data)
def test_negative_patch_user(id, data):
    response = requests.patch(f"{HOST}/api/users/", data)
    assert response.status_code == 200
    validate(instance=response.json(), schema=update_user_schema)
