import requests

def test_users_api():

    response = requests.get(
        "https://jsonplaceholder.typicode.com/users"
    )

    assert response.status_code == 200
