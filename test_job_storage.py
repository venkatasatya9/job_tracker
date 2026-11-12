from job_storage import JobStorage

def test_save_and_load_jobs(tmp_path):
    # Arrange
    file_path = tmp_path / "test_jobs.json"
    storage = JobStorage(str(file_path))

    jobs = [
        {
            "id": 1,
            "company": "Microsoft",
            "role": "Data Engineer",
            "location": "Remote",
            "status": "Applied"
        }
    ]

    # Act
    storage.save_jobs(jobs)
    loaded_jobs = storage.load_jobs()

    # Assert
    assert loaded_jobs == jobs

def test_load_jobs_when_file_does_not_exist(tmp_path):
    # Arrange
    file_path = tmp_path / "missing_jobs.json"
    storage = JobStorage(str(file_path))

    # Act
    jobs = storage.load_jobs()

    # Assert
    assert jobs == []
