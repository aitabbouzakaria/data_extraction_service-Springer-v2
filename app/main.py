from fastapi import FastAPI
from app.routes import scan, jobs, health

app = FastAPI(title="githubprjt API")

app.include_router(scan.router)
app.include_router(jobs.router)
app.include_router(health.router)

@app.get("/")
async def root():
    return {"message": "githubprjt running"}
