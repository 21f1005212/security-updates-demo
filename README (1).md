# Automated Security Updates Demo

A Python API project configured with **Dependabot** for automated dependency security updates.

**Contact:** 21f1005212@ds.study.iitm.ac.in  
**Student ID:** 21f1005212 | IIT Madras · BSc Data Science & Applications

---

## About

This repository demonstrates automated dependency management using GitHub's Dependabot.
When a CVE is disclosed for any dependency, Dependabot automatically opens a PR within
24 hours — keeping the project secure without manual monitoring.

## Project Structure

```
├── main.py              # FastAPI application entry point
├── requirements.txt     # Python dependencies
├── .github/
│   └── dependabot.yml   # Automated dependency update config
└── README.md
```

## Dependencies

| Package   | Version  | Purpose                        |
|-----------|----------|--------------------------------|
| fastapi   | 0.104.1  | Modern async web framework     |
| requests  | 2.31.0   | HTTP client library            |
| pandas    | 2.1.3    | Data analysis and manipulation |
| uvicorn   | 0.24.0   | ASGI server for FastAPI        |
| pydantic  | 2.5.0    | Data validation                |

## Dependabot Configuration

Dependabot is configured to:
- **Ecosystem:** `pip` (Python packages)
- **Schedule:** Weekly scans for outdated/vulnerable dependencies
- **PR prefix:** `deps` — e.g. `deps: bump requests from 2.31.0 to 2.32.0`

## Why This Matters

A production API was using a vulnerable version of the `requests` library for **6 months**
before it was caught manually. With Dependabot configured, that same vulnerability would
have triggered an automatic PR within **24 hours** of CVE disclosure.

## Setup

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

---

*21f1005212@ds.study.iitm.ac.in — IIT Madras Online Degree Programme*
