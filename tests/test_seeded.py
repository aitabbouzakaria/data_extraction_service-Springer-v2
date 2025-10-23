from fastapi.testclient import TestClient
from app.main import app
from app.routes.scan import jobs_db, create_job, simulate_job_completion

client = TestClient(app)

def setup_module(module):
    """Prepare seeded test data"""
    jobs_db.clear()
    completed_job = create_job(status="in_progress")
    simulate_job_completion(completed_job)
    pending_job = create_job(status="pending")
    cancelled_job = create_job(status="cancelled")

def test_list_all_jobs():
    response = client.get("/api/v1/jobs/jobs")
    assert response.status_code == 200
    data = response.json()
    assert "jobs" in data
    assert data["total_jobs"] >= 3

def test_get_statistics():
    response = client.get("/api/v1/jobs/statistics")
    assert response.status_code == 200
    stats = response.json()["statistics"]
    assert "completed_jobs" in stats
    assert stats["total_jobs"] >= 3

def test_get_seeded_completed_job_result():
    completed_job = next(job_id for job_id, job in jobs_db.items() if job["status"] == "completed")
    response = client.get(f"/api/v1/scan/result/{completed_job}")
    assert response.status_code == 200
    records = response.json()["records"]
    assert isinstance(records, list)
    assert len(records) > 0

def test_health_check():
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
