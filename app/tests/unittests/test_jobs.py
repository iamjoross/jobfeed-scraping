def test_request_job_boards_all(client):
    response = client.get("/job-boards/all")
    assert response.status_code == 200

def test_request_job_delete(client):
    response = client.delete("/job/1")
    assert response.status_code == 200

