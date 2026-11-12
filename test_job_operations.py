import pytest
from unittest.mock import Mock

from job_storage import JobStorage
from job_operations import JobOperations

@pytest.fixture
def operations(tmp_path):
    file_path = tmp_path / "test_jobs.json"

    job_storage = JobStorage(str(file_path))

    return JobOperations(job_storage)

def add_sample_job(operations):
    jobs = [
        {
            "id": 1,
            "company": "Microsoft",
            "role": "Data Engineer",
            "location": "Remote",
            "status": "Applied"
        },
        {
            "id": 2,
            "company": "Amazon",
            "role": "Python Developer",
            "location": "Atlanta",
            "status": "Interview"
        }
    ]

    operations.job_storage.save_jobs(jobs)

def test_add_job(operations, monkeypatch):
    inputs = iter([
        "Google",
        "Data Engineer",
        "Remote",
        "Applied"
    ])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    operations.add_job()

    jobs = operations.job_storage.load_jobs()

    assert len(jobs) == 1
    assert jobs[0]["id"] == 1
    assert jobs[0]["company"] == "Google"
    assert jobs[0]["role"] == "Data Engineer"

def test_add_job_with_empty_company(operations, monkeypatch, capsys):
    inputs = iter(["", "Data Engineer", "Remote", "Applied"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    operations.add_job()

    jobs = operations.job_storage.load_jobs()

    assert jobs == []
    assert "All fields are required" in capsys.readouterr().out

def test_view_jobs(operations, capsys):
    add_sample_job(operations)

    operations.view_jobs()

    output = capsys.readouterr().out

    assert "Microsoft" in output
    assert "Amazon" in output
    assert "Data Engineer" in output

def test_search_jobs(operations, monkeypatch, capsys):
    add_sample_job(operations)

    monkeypatch.setattr("builtins.input", lambda _: "microsoft")

    operations.search_jobs()

    output = capsys.readouterr().out

    assert "Microsoft" in output
    assert "Amazon" not in output

def test_update_job_status(operations, monkeypatch):
    add_sample_job(operations)

    inputs = iter(["1", "Interview"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    operations.update_job_status()

    jobs = operations.job_storage.load_jobs()

    assert jobs[0]["status"] == "Interview"

def test_delete_job(operations, monkeypatch):
    add_sample_job(operations)

    inputs = iter(["1", "yes"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    operations.delete_job()

    jobs = operations.job_storage.load_jobs()

    assert len(jobs) == 1
    assert jobs[0]["company"] == "Amazon"

def test_delete_job_cancelled(operations, monkeypatch):
    add_sample_job(operations)

    inputs = iter(["1", "no"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    operations.delete_job()

    jobs = operations.job_storage.load_jobs()

    assert len(jobs) == 2


def test_view_jobs_when_empty(operations, capsys):
    operations.view_jobs()

    output = capsys.readouterr().out

    assert "No job applications found" in output


def test_search_jobs_no_match(operations, monkeypatch, capsys):
    add_sample_job(operations)

    monkeypatch.setattr("builtins.input", lambda _: "Netflix")

    operations.search_jobs()

    output = capsys.readouterr().out

    assert "No matching jobs found" in output


def test_update_job_with_invalid_id(operations, monkeypatch, capsys):
    add_sample_job(operations)

    monkeypatch.setattr("builtins.input", lambda _: "abc")

    operations.update_job_status()

    output = capsys.readouterr().out

    assert "Invalid ID" in output

    jobs = operations.job_storage.load_jobs()

    assert jobs[0]["status"] == "Applied"


def test_update_job_id_not_found(operations, monkeypatch, capsys):
    add_sample_job(operations)

    monkeypatch.setattr("builtins.input", lambda _: "999")

    operations.update_job_status()

    output = capsys.readouterr().out

    assert "Job ID not found" in output


def test_delete_job_id_not_found(operations, monkeypatch, capsys):
    add_sample_job(operations)

    monkeypatch.setattr("builtins.input", lambda _: "999")

    operations.delete_job()

    output = capsys.readouterr().out

    assert "Job ID not found" in output

    jobs = operations.job_storage.load_jobs()

    assert len(jobs) == 2

def test_update_job_status_with_mock(monkeypatch):
    # Arrange
    mock_storage = Mock()

    mock_storage.load_jobs.return_value = [
        {
            "id": 1,
            "company": "Microsoft",
            "role": "Data Engineer",
            "location": "Remote",
            "status": "Applied"
        }
    ]

    operations = JobOperations(mock_storage)

    inputs = iter(["1", "Interview"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    # Act
    operations.update_job_status()

    # Assert
    saved_jobs = mock_storage.save_jobs.call_args[0][0]

    assert saved_jobs[0]["status"] == "Interview"

    mock_storage.load_jobs.assert_called_once()
    mock_storage.save_jobs.assert_called_once()
