# Industrial Safety Monitoring System

A Python application that reads **temperature, gas concentration, smoke and pressure** values from an industrial environment and classifies the workplace condition as **SAFE**, **WARNING** or **EMERGENCY**. A Jenkins pipeline runs parameterized tests for each industrial environment and publishes an HTML safety report.

## How it works

Each environment has a warning limit and an emergency limit for every sensor.

| Environment    | Temperature (°C) | Gas (ppm) | Smoke (%) | Pressure (bar) |
|----------------|------------------|-----------|-----------|----------------|
| chemical_plant | 60 / 80          | 25 / 50   | 5 / 15    | 8 / 10         |
| boiler_room    | 90 / 120         | 20 / 40   | 5 / 12    | 10 / 15        |

*(Format: warning / emergency)*

Classification rules:

1. A sensor value at or above its **emergency** limit gives **EMERGENCY**.
2. A sensor value at or above its **warning** limit gives **WARNING**.
3. **Fire rule:** if temperature and smoke are both at warning level or above, the result is **EMERGENCY**.
4. Otherwise the result is **SAFE**.
5. A negative sensor value raises a `ValueError`.

## Project structure

```
industrial-safety-monitor/
├── safety.py          # classification logic and environment limits
├── test_safety.py     # parameterized pytest tests
├── Jenkinsfile        # Jenkins pipeline definition
├── requirements.txt   # Python dependencies
└── README.md
```

## Run locally

```bash
python -m venv .venv
source .venv/Scripts/activate      # Git Bash on Windows
python -m pip install -r requirements.txt
python -m pytest -v
```

Run the tests for a single environment:

```bash
python -m pytest -v -k boiler_room
```

Generate the HTML report:

```bash
python -m pytest --html=reports/safety_report.html --self-contained-html
```

## Parameterized testing

`test_safety.py` uses `@pytest.mark.parametrize` so one test function runs against many readings and environments, including boundary values (exactly at the warning limit), the fire rule and invalid input.

## Jenkins pipeline

The `Jenkinsfile` defines a pipeline with an `ENVIRONMENT` choice parameter (`chemical_plant` or `boiler_room`).

1. **Setup:** creates a virtual environment and installs the requirements.
2. **Run Parameterized Tests:** runs pytest for the selected environment and writes `reports/report_<ENVIRONMENT>.html`.
3. **Post action:** publishes the HTML report with the HTML Publisher plugin. It appears as **Safety Report - <ENVIRONMENT>** on the build page.

### Jenkins setup

1. Install Jenkins and the **HTML Publisher** plugin.
2. Create a **Pipeline** job with *Pipeline script from SCM*.
3. Repository URL: `https://github.com/Thenmozhi-eng/industrial-safety-monitor.git`, branch `*/master`, script path `Jenkinsfile`.
4. Use **Build with Parameters** and choose the environment.

## Tech stack

Python, pytest, pytest-html, Git, GitHub, Jenkins