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
    
    
def test_teams_status_code():
    response = requests.get(f"{BASE_URL}/competitions/WC/teams", headers=HEADERS)
    assert response.status_code == 200


def test_teams_count():
    response = requests.get(f"{BASE_URL}/competitions/WC/teams", headers=HEADERS)
    data = response.json()
    assert len(data["teams"]) == 48
    
    
def test_first_team_has_name():
    response = requests.get(f"{BASE_URL}/competitions/WC/teams", headers=HEADERS)
    data = response.json()
    assert data["teams"][0]
    
def test_teams_no_token():
    response = requests.get(f"{BASE_URL}/competitions/WC/teams")
    assert response.status_code in [401, 403]
    
def test_match_has_status():
    response = requests.get(f"{BASE_URL}/competitions/WC/matches", headers=HEADERS)
    data = response.json()
    assert "status" in data["matches"][0]