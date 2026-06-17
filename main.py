from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Andrew Happ Portfolio API")

# Ensure CORS is configured so your frontend port (e.g. 5173 template) can fetch it
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://portfolio-frontend-one-umber.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Portfolio API is running"}

@app.get("/projects")
def get_projects():
    return [
        {
            "id": 1,
            "title": "Dr. Kenneth Harling Case Competition (Coffee App)",
            "role": "Full-Stack Application Developer",
            "duration": "Mar. 2026 – May 2026",
            "location": "West Lafayette, IN",
            "description": "Developed and deployed a full‑stack cloud application integrating Google BigQuery and Cloud Run with FastAPI. Engineered REST API endpoints supporting location and menu data queries to support real‑time multi‑location logistics.",
            "skills": ["Python", "FastAPI", "BigQuery", "Cloud Run", "REST APIs", "SQL"]
        },
        {
            "id": 2,
            "title": "Purdue Quantitative Methods Showcase",
            "role": "Predictive Analytics Researcher",
            "duration": "Feb. 2026 – May 2026",
            "location": "West Lafayette, IN",
            "description": "Developed supervised machine learning models to predict health insurance beneficiary medical charges. Evaluated multi-algorithmic pricing models using rigorous cross-validation to inform dynamic pricing strategies.",
            "skills": ["Python", "R", "Predictive Modeling", "Machine Learning", "Data Analysis", "Supervised Learning"]
        },
        {
            "id": 3,
            "title": "Purdue Spring Undergraduate Research Conference",
            "role": "Time Series & Machine Learning Analyst",
            "duration": "Jan. 2026 – Apr. 2026",
            "location": "West Lafayette, IN",
            "description": "Built end-to-end forecasting systems with Random Forest, SARIMA, and Linear Regression targeting weekly sales at 45 Walmart stores. Engineered custom lag, seasonal, and holiday features, presenting findings to peer and faculty panels.",
            "skills": ["Python", "Machine Learning", "Forecasting", "Random Forest", "SARIMA", "Time Series"]
        },
        {
            "id": 4,
            "title": "Isle of Palms BC Company",
            "role": "Inventory Control & Operations Coordinator",
            "duration": "May 2025 – Aug. 2025",
            "location": "Charleston, SC",
            "description": "Managed warehouse inventory distribution to coordinate peak consumer demand flows. Analyzed layout and storage logistics to increase total site throughput and minimize stock disparities using MS Excel.",
            "skills": ["Operations Management", "Inventory Control", "Data Analysis", "Microsoft Excel", "Logistics", "Supply Chain"]
        }
    ]