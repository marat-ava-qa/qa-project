import requests
import os

TOKEN = os.getenv("FOOTBALL_TOKEN")
HEADERS = {"X-Auth-Token": TOKEN}
BASE_URL = "https://api.football-data.org/v4"


def test_world_cup_exists():
    response = requests.get(f"{BASE_URL}/competitions/WC", headers=HEADERS)
    assert response.status_code == 200


def test_world_cup_name():
    response = requests.get(f"{BASE_URL}/competitions/WC", headers=HEADERS)
    data = response.json()
    assert data["name"] == "FIFA World Cup"


def test_unknown_competition():
    response = requests.get(f"{BASE_URL}/competitions/XXXX", headers=HEADERS)
    assert response.status_code == 404