from fastapi import APIRouter
from typing import Dict, Any
from datetime import datetime
from app.routes.scan import jobs_db  # reuse the in-memory database

router = APIRouter()

# -------------------------------
# 1️ List all jobs
# -------------------------------
@router.get("/jobs")
def list_all_jobs():
    if not jobs_db:
        return {"message": "No jobs found", "jobs": []}
    return {"total_jobs": len(jobs_db), "jobs": list(jobs_db.values())}


# -------------------------------
# 2️ Get job statistics
# -------------------------------
@router.get("/statistics")
def job_statistics():
    if not jobs_db:
        return {"message": "No jobs found", "statistics": {}}

    total_jobs = len(jobs_db)
    completed = sum(1 for job in jobs_db.values() if job["status"] == "completed")
    pending = sum(1 for job in jobs_db.values() if job["status"] == "pending")
    cancelled = sum(1 for job in jobs_db.values() if job["status"] == "cancelled")
    failed = sum(1 for job in jobs_db.values() if job["status"] == "failed")

    stats = {
        "total_jobs": total_jobs,
        "completed_jobs": completed,
        "pending_jobs": pending,
        "cancelled_jobs": cancelled,
        "failed_jobs": failed,
        "last_updated": datetime.utcnow().isoformat()
    }

    return {"statistics": stats}
