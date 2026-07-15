import requests

URL = "https://jsonplaceholder.typicode.com/users"


def test_create_user():
    new_user = {"name": "Marat", "job": "QA Engineer"}
    response = requests.post(URL, json=new_user)

    assert response.status_code == 201

    data = response.json()
    assert data["name"] == "Marat"
    assert data["job"] == "QA Engineer"
    assert "id" in data
    
    
def test_create_order():
    new_order = {"product": "football", "quantity": 2}
    response = requests.post(URL, json=new_order)
    
    assert response.status_code == 201
    
    data = response.json()
    assert data["product"] == "football"
    assert "id" in data