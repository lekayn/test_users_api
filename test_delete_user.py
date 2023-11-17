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
    # здесь и в функции ниже следует добавить проверку на то, что пользователь действительно удалился
    # Например запросом get api/users/{id}
    # но на сайте вероятно нет связи данных бд сервера
    # с добавляемыми/удаляемыми данными от клиента. Эти данные как будто не добавляются в БД
    # по таким запросам приходит всегда один ответ - что юзер добавлен, удален, не пишет никаких ошибок
    # Поэтому такой проверки тут нет


@pytest.mark.parametrize("id", negative_id)
def test_negative_get_users(id):
    response = requests.delete(f"{HOST}/api/users")
    assert response.status_code == 204
