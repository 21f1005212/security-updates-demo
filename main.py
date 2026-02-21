from fastapi import FastAPI
import requests
import pandas as pd

app = FastAPI(title="Security Updates Demo API")


@app.get("/")
def root():
    return {"message": "API is running", "student": "21f1005212"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/dependencies")
def list_dependencies():
    deps = [
        {"name": "fastapi", "purpose": "Web framework"},
        {"name": "requests", "purpose": "HTTP client"},
        {"name": "pandas", "purpose": "Data analysis"},
        {"name": "uvicorn", "purpose": "ASGI server"},
        {"name": "pydantic", "purpose": "Data validation"},
    ]
    return {"dependencies": deps, "count": len(deps)}
