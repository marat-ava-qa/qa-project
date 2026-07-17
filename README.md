# ⚽ Football QA Automation Framework

![Tests](https://github.com/marat-ava-qa/qa-project/actions/workflows/tests.yml/badge.svg)

📊 **[Live Allure Report](https://marat-ava-qa.github.io/qa-project/)**

Python test automation framework for the FIFA World Cup 2026 API
(football-data.org) and UI scenarios. Tests run automatically on every
push via GitHub Actions, reports are published to GitHub Pages.

## Tech Stack

- Python, pytest (fixtures, parametrization, markers)
- requests — API testing
- Selenium + Page Object Model — UI testing (headless)
- GitHub Actions — CI
- Allure — reporting

## Test Coverage

**API (World Cup 2026):**
- status codes and response structure: /competitions, /teams, /matches
- data validation: verify the tournament contains exactly 48 teams — the real-world format of World Cup 2026, the first tournament with the expanded field
- negative scenarios: unknown competition (404), request without token (401/403)

**UI (saucedemo.com):**
- login flow: success, wrong password, element visibility
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
Testing real World Cup 2026 data keeps the work genuinely interesting.