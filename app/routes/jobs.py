from fastapi import APIRouter

router = APIRouter(prefix="/jobs", tags=["jobs"]) 

@router.get("/")
async def list_jobs():
    """Return a list of jobs (placeholder data)."""
    return {"jobs": []}

@router.get("/{job_id}")
async def get_job(job_id: str):
    return {"job_id": job_id, "status": "unknown"}
