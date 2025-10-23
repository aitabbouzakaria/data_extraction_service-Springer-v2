from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_real_extraction_workflow():
    # 1. Start extraction
    response = client.post("/api/v1/scan/start", json={"api_token": "valid_token_123"})
    assert response.status_code == 200 or response.status_code == 202
    data = response.json()
    job_id = data["job_id"]

    # 2. Check job status
    status_response = client.get(f"/api/v1/scan/status/{job_id}")
    assert status_response.status_code == 200
    assert status_response.json()["status"] in ["completed", "in_progress"]

    # 3. Get job result
    result_response = client.get(f"/api/v1/scan/result/{job_id}")
    assert result_response.status_code == 200
    result_data = result_response.json()
    assert "records" in result_data
    assert isinstance(result_data["records"], list)

    # 4. Remove job data
    remove_response = client.delete(f"/api/v1/scan/remove/{job_id}")
    assert remove_response.status_code in [200, 204]
