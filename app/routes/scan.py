from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import uuid
from typing import Dict, Any
from datetime import datetime

router = APIRouter()

# -------------------------------
# In-memory job database (mock)
# -------------------------------
jobs_db: Dict[str, Dict[str, Any]] = {}

# -------------------------------
# Models
# -------------------------------
class StartJobRequest(BaseModel):
    api_token: str

class ExtractionResult(BaseModel):
    id_from_service: str
    email: str
    first_name: str
    last_name: str


# -------------------------------
# Helper functions
# -------------------------------
def create_job(status="pending"):
    job_id = str(uuid.uuid4())
    jobs_db[job_id] = {
        "job_id": job_id,
        "status": status,
        "created_at": datetime.utcnow().isoformat(),
        "updated_at": datetime.utcnow().isoformat(),
        "records": []
    }
    return job_id


def simulate_job_completion(job_id: str):
    # Simulate data extraction
    jobs_db[job_id]["status"] = "completed"
    jobs_db[job_id]["updated_at"] = datetime.utcnow().isoformat()
    jobs_db[job_id]["records"] = [
        {
            "id_from_service": "A123",
            "email": "user@example.com",
            "first_name": "John",
            "last_name": "Doe"
        },
        {
            "id_from_service": "B456",
            "email": "jane@example.com",
            "first_name": "Jane",
            "last_name": "Smith"
        }
    ]


# -------------------------------
# 1️ Start new extraction
# -------------------------------
@router.post("/start")
def start_extraction(req: StartJobRequest):
    if not req.api_token or req.api_token.strip() == "":
        raise HTTPException(status_code=400, detail="Missing or invalid API token")

    # Simulate a new job creation
    job_id = create_job(status="in_progress")

    # Simulate it finishing quickly
    simulate_job_completion(job_id)

    return {"job_id": job_id, "status": "completed", "message": "Job started and completed successfully"}


# -------------------------------
# 2️ Get job status
# -------------------------------
@router.get("/status/{job_id}")
def get_job_status(job_id: str):
    job = jobs_db.get(job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job ID not found")
    return {"job_id": job_id, "status": job["status"], "updated_at": job["updated_at"]}


# -------------------------------
# 3️ Get job results
# -------------------------------
@router.get("/result/{job_id}")
def get_job_result(job_id: str):
    job = jobs_db.get(job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job ID not found")

    if job["status"] != "completed":
        raise HTTPException(status_code=409, detail="Job not completed yet")

    return {"job_id": job_id, "records": job["records"]}


# -------------------------------
# 4️ Cancel a job
# -------------------------------
@router.post("/cancel/{job_id}")
def cancel_job(job_id: str):
    job = jobs_db.get(job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job ID not found")

    if job["status"] in ["completed", "failed"]:
        raise HTTPException(status_code=409, detail="Cannot cancel a completed or failed job")

    job["status"] = "cancelled"
    job["updated_at"] = datetime.utcnow().isoformat()
    return {"job_id": job_id, "status": "cancelled"}


# -------------------------------
# 5️ Remove job data
# -------------------------------
@router.delete("/remove/{job_id}")
def remove_job(job_id: str):
    if job_id not in jobs_db:
        raise HTTPException(status_code=404, detail="Job ID not found")

    del jobs_db[job_id]
    return {"message": f"Job {job_id} and associated data removed"}
