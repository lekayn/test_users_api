import requests
import pytest
from jsonschema import validate

HOST = "https://reqres.in"
create_user_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "job": {"type": "string"},
        "id": {"type": "string"},
        "createdAt": {"type": "string"},
    },
    "required": ["name", "job", "id", "createdAt"]
}
negative_create_user_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "job": {"type": "string"},
        "id": {"type": "string"},
        "createdAt": {"type": "string"},
    },
    "required": ["id", "createdAt"]
}
positive_data = [{"name": "George", "job": "lead_testerrr"},
                 {"name": "Olga", "job": "load_testerrr"},
                 {"name": "Victor", "job": "fun_testerrr"},
                 ]
negative_data = [{"name": "\n\n\n", "job": "\t\t\t\t"},
                 {
                     "name": "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffv",
                     "job": "12"},
                 {"go": 312, "id": 142, "name": "yo", "das": "dasdkfdfj!!32"},
                 {1: 2, 3: 5, 0: ""},
                 {}
                 ]


@pytest.mark.parametrize("data", positive_data)
def test_positive_post_user(data):
    response = requests.post(f"{HOST}/api/users/", data)
    assert response.status_code == 201
    validate(instance=response.json(), schema=create_user_schema)
    # здесь следовало бы добавить проверку на то, что юзер действительно создался, но
    # при запросе получить всех юзеров GET api/users, сервер выдает всегда один и тот же список
    # хотя и наотправлял новых через POST.
    # вероятно, что стоит заглушка. Поэтому такой проверки нет


@pytest.mark.parametrize("data", negative_data)
def test_negative_post_user(data):
    response = requests.post(f"{HOST}/api/users/", data)
    assert response.status_code == 201
    validate(instance=response.json(), schema=negative_create_user_schema)
    # по этому запросу можно отсылать любые данные, нет обработки ошибочных данных на сервере
    # кушает всё