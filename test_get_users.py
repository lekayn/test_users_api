import requests
import pytest
from jsonschema import validate

HOST = "https://reqres.in"
get_users_schema = {
    "type": "object",
    "properties": {
        "page": {"type": "number"},
        "per_page": {"type": "number"},
        "data": {"type": "array"},
    },
    "required": ["page", "per_page", "data"]
}
positive_params = [{"page": "", "per_page": ""},
                   {"page": 1, "per_page": 10},
                   {"page": 2},
                   ]
negative_params = [{"page": "\n!!!;;:::", "per_page": 6},
                   {"page": 2147483647, "per_page": 6},
                   {"page": 2147483648, "per_page": 6},
                   {"page": 0, "per_page": 6},
                   {"page": -1, "per_page": 6},
                   {"page": 1, "per_page": 6},
                   {"page": 1, "per_page": 0},
                   {"page": 1, "per_page": -1},
                   {"page": 1, "per_page": 2147483647},
                   {"page": 1, "per_page": 2147483648},
                   ]


@pytest.mark.parametrize("params", positive_params)
def test_positive_get_users(params):
    response = requests.get(f"{HOST}/api/users", params=params)
    assert response.status_code == 200
    validate(instance=response.json(), schema=get_users_schema)


@pytest.mark.parametrize("params", negative_params)
def test_negative_get_users(params):
    response = requests.get(f"{HOST}/api/users", params=params)
    assert response.status_code == 200
    validate(instance=response.json(), schema=get_users_schema)