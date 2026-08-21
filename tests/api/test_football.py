import requests
import os
import pytest
import time

TOKEN = os.getenv("FOOTBALL_TOKEN")
HEADERS = {"X-Auth-Token": TOKEN}
BASE_URL = "https://api.football-data.org/v4"

def get_with_retry(url, headers, retries=5):
    for attempt in range(retries):             
        response = requests.get(url, headers=headers)
        if response.status_code != 429:         
            return response                       
        time.sleep(10)                            
    return response 


@pytest.mark.parametrize("league", ["WC", "PD", "PL", "CL"])
def test_league_exists(league):
    response = get_with_retry(f"{BASE_URL}/competitions/{league}", headers=HEADERS)
    assert response.status_code == 200
                        
                                                    
def test_world_cup_name():
    response = get_with_retry(f"{BASE_URL}/competitions/WC", headers=HEADERS)
    data = response.json()
    assert data["name"] == "FIFA World Cup"


def test_unknown_competition():
    response = get_with_retry(f"{BASE_URL}/competitions/XXXX", headers=HEADERS)
    assert response.status_code == 404
    
    
def test_teams_status_code():
    response = get_with_retry(f"{BASE_URL}/competitions/WC/teams", headers=HEADERS)
    assert response.status_code == 200


def test_teams_count():
    response = get_with_retry(f"{BASE_URL}/competitions/WC/teams", headers=HEADERS)
    data = response.json()
    assert len(data["teams"]) == 48
    
    
def test_first_team_has_name():
    response = get_with_retry(f"{BASE_URL}/competitions/WC/teams", headers=HEADERS)
    data = response.json()
    assert "name" in data["teams"][0]
    
def test_teams_no_token():
    response = get_with_retry(f"{BASE_URL}/competitions/WC/teams", headers={})
    assert response.status_code in [401, 403]
    
def test_match_has_status():
    response = get_with_retry(f"{BASE_URL}/competitions/WC/matches", headers=HEADERS)
    data = response.json()
    assert "status" in data["matches"][0]

# LA LIGA     
def test_la_liga_teams_count():
    response = get_with_retry(f"{BASE_URL}/competitions/PD/teams", headers=HEADERS)
    data = response.json()
    assert len(data["teams"]) == 20

def test_la_liga_first_team_has_name():
    response = get_with_retry(f"{BASE_URL}/competitions/PD/teams", headers=HEADERS)
    data = response.json()
    assert "name" in data["teams"][0]
    

def test_la_liga_match_has_status():
    response = get_with_retry(f"{BASE_URL}/competitions/PD/matches", headers=HEADERS)
    data = response.json()
    assert "status" in data["matches"][0]
    
# APL
def test_premier_league_match_has_status():
    response = get_with_retry(f"{BASE_URL}/competitions/PD/matches", headers=HEADERS)
    data = response.json()
    assert "status" in data["matches"][0]