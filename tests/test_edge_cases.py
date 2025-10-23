
from fastapi.testclient import TestClient
from app.main import app
from app.routes.scan import jobs_db, create_job

client = TestClient(app)

def test_start_with_invalid_token():
    response = client.post("/api/v1/scan/start", json={"api_token": ""})
    assert response.status_code == 400
    assert "invalid API token" in response.text

def test_nonexistent_job_status():
    response = client.get("/api/v1/scan/status/nonexistent123")
    assert response.status_code == 404

def test_access_result_for_incomplete_job():
    job_id = create_job(status="pending")
    response = client.get(f"/api/v1/scan/result/{job_id}")
    assert response.status_code == 409
    assert "not completed yet" in response.text

def test_cancel_completed_job():
    job_id = create_job(status="completed")
    response = client.post(f"/api/v1/scan/cancel/{job_id}")
    assert response.status_code == 409

def test_remove_nonexistent_job():
    response = client.delete("/api/v1/scan/remove/fake123")
    assert response.status_code == 404
