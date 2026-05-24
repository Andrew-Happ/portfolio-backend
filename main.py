from fastapi import FastAPI

app = FastAPI(title="Andrew Happ Portfolio API")

@app.get("/")
def home():
    return {"message": "Portfolio API is running"}

@app.get("/projects")
def get_projects():
    return [
        {
            "id": 1,
            "title": "Uncle Joe's Coffee App",
            "description": "Full-stack coffee shop app using FastAPI, BigQuery, and Cloud Run.",
            "skills": ["Python", "FastAPI", "BigQuery", "Cloud Run"]
        },
        {
            "id": 2,
            "title": "Walmart Sales Forecasting",
            "description": "Predictive analytics project forecasting weekly store sales.",
            "skills": ["Python", "Machine Learning", "Forecasting", "Data Analysis"]
        }
    ]