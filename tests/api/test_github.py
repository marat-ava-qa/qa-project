import requests

URL = "https://api.github.com/users/marat-ava-qa"


def test_status_code():
    response = requests.get(URL)
    assert response.status_code == 200


def test_login():
    response = requests.get(URL)
    data = response.json()
    assert data["login"] == "marat-ava-qa"


def test_user_not_found():
    response = requests.get("https://api.github.com/users/this-user-does-not-exist-99887766")
    assert response.status_code == 404