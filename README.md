# ⚽ Football QA Automation Framework

![Tests](https://github.com/marat-ava-qa/qa-project/actions/workflows/tests.yml/badge.svg)

📊 **[Live Allure Report](https://marat-ava-qa.github.io/qa-project/)**

Python test automation framework for football data APIs (football-data.org) —
covering multiple competitions: FIFA World Cup, La Liga, Premier League, and
Champions League. Includes API tests, UI tests, and retry logic for handling
rate limits. Tests run automatically on every push via GitHub Actions, with
reports published to GitHub Pages.

## Tech Stack

- Python, pytest (fixtures, parametrization, markers)
- requests — API testing
- Selenium + Page Object Model — UI testing (headless)
- GitHub Actions — CI
- Allure — reporting

## Test Coverage

**API (football-data.org):**
- multiple competitions tested via parametrization (World Cup, La Liga, Premier League, Champions League)
- status codes and response structure: /competitions, /teams, /matches
- data validation: verify each league has the correct number of teams
- negative scenarios: unknown competition (404), request without token (401/403)
- retry mechanism for API rate limiting (429) and network errors
- fixtures to reduce duplicate API calls

**UI (saucedemo.com):**
- login flow: success, wrong password, element visibility
- add to cart flow
- Page Object Model, explicit waits (WebDriverWait)

## How to Run

```bash
git clone https://github.com/marat-ava-qa/qa-project.git
cd qa-project
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
export FOOTBALL_TOKEN="your_token_from_football-data.org"
pytest tests/ -v
```

## About the Author

I'm Marat, a QA Automation Engineer and a lifelong football fan.
I built this framework from scratch — Python, pytest, API and UI test
layers, CI/CD pipeline with GitHub Actions, and live Allure reporting.
Testing real football data keeps the work genuinely interesting.