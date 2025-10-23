from fastapi import FastAPI
from app.routes import scan, jobs, health

app = FastAPI(title="Data Extraction Service", version="1.0")

app.include_router(scan.router, prefix="/api/v1/scan", tags=["Scan"])
app.include_router(jobs.router, prefix="/api/v1/jobs", tags=["Jobs"])
app.include_router(health.router, prefix="/api/v1/health", tags=["Health"])

@app.get("/")
def root():
    return {
        "message": "Data Extraction Service API is running 🚀",
        "endpoints": [
            "/api/v1/scan/start",
            "/api/v1/scan/status/<job_id>",
            "/api/v1/scan/result/<job_id>",
            "/api/v1/scan/cancel/<job_id>",
            "/api/v1/scan/remove/<job_id>",
            "/api/v1/jobs/jobs",
            "/api/v1/jobs/statistics",
            "/api/v1/health"
        ]
    }
