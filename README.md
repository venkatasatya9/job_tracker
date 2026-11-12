# Job Search Tracker

A command-line Python application for managing job applications using an object-oriented, modular architecture. The application allows users to add, view, search, update, and delete job applications. It stores application records in a JSON file so that information is preserved between sessions.

## Features

- **Add Job:** Add a job application with a unique ID, company, role, location, and application status.
- **View Jobs:** Display all saved job applications.
- **Search Jobs:** Search applications by company name.
- **Update Job Status:** Update an application using its unique Job ID.
- **Delete Job:** Delete a specific application using its Job ID, with a confirmation step.
- **Persistent Storage:** Save and load job applications using JSON.
- **Modular Architecture:** Separate application interface, business logic, and data storage into independent Python classes.
- **Automated Testing:** Validate application functionality using pytest.
- **Test Coverage:** Measure code coverage using pytest-cov.

## Technologies

- Python 3.12
- Object-Oriented Programming (OOP)
- JSON
- Pytest
- Pytest-cov
- Git and GitHub
- Python Virtual Environments

## Project Structure

```text
taskmanager/
│
├── job_tracker.py          # Main application and menu interface
├── job_operations.py       # Job application business logic and CRUD operations
├── job_storage.py          # JSON file loading and saving functionality
│
├── test_job_operations.py  # Unit tests for job operations
├── test_job_storage.py     # Unit tests for JSON storage
│
├── jobs.json               # Local job application data (not committed)
├── README.md               # Project documentation
├── requirements.txt        # Python dependencies
└── .gitignore              # Files excluded from Git
```

Additional test-generated directories and files:

- `.pytest_cache/` - Pytest cache.
- `.coverage` - Coverage measurement data.
- `htmlcov/` - HTML coverage report.

These generated files are excluded from Git.

## Architecture and Design

The application follows the **Separation of Concerns** principle by dividing responsibilities among three classes.

### 1. JobTracker

- Acts as the main application entry point.
- Displays the command-line menu.
- Collects user selections.
- Delegates job operations to the `JobOperations` class.

### 2. JobOperations

- Contains the business logic for managing job applications.
- Implements Create, Read, Update, and Delete (CRUD) operations.
- Communicates with `JobStorage` to retrieve and persist job records.
- Handles user input and validation.

### 3. JobStorage

- Handles JSON file operations.
- Loads job application records.
- Saves updated job application records.
- Handles missing and invalid JSON files.
- Supports generating IDs for older records without IDs.

### Composition and Dependency Injection

The application uses composition to connect its components.

`JobTracker` creates a `JobStorage` object and passes it to `JobOperations`.

This approach promotes code reuse, maintainability, and easier unit testing.

## Requirements

- Python 3.12 or compatible Python version.
- pip package manager.
- Pytest and pytest-cov for automated testing.

The core Job Search Tracker application uses Python's built-in `json` module and does not require third-party packages to run.

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/venkatasatya9/job_tracker.git
```

Navigate to the project directory:

```bash
cd taskmanager
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

Windows PowerShell:

```powershell
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

If you only want to run the application, installing pytest and pytest-cov is optional.

## How to Run the Application

Execute:

```bash
python job_tracker.py
```

## Application Menu

```text
===== JOB SEARCH TRACKER =====
1. Add Job
2. View Jobs
3. Search Jobs
4. Update Job Status
5. Delete Job
6. Exit
```

Follow the prompts to manage your job applications.

## Data Storage

Job applications are stored locally in `jobs.json`.

Each record contains:

- `id`: Unique job application ID.
- `company`: Company name.
- `role`: Job title.
- `location`: Job location.
- `status`: Application status.

Example:

```json
{
    "id": 1,
    "company": "Microsoft",
    "role": "Data Engineer",
    "location": "Atlanta",
    "status": "Interview"
}
```

The application automatically assigns IDs to older records that do not already have one.

**Privacy note:** `jobs.json` contains personal application information. It is excluded from Git so that your private job-search data is not uploaded to the public repository.

## Automated Testing

The project uses **pytest** to test individual components and validate application functionality.

### Run All Tests

```bash
pytest -v
```

### Test Coverage

The project uses `pytest-cov` to measure code coverage.

Run:

```bash
pytest --cov=job_storage --cov=job_operations --cov-report=term-missing
```

### Generate an HTML Coverage Report

```bash
pytest --cov=job_storage --cov=job_operations --cov-report=html
```

Open the report in your browser:

```powershell
start htmlcov/index.html
```

### Testing Concepts Implemented

- Unit testing
- Positive and negative test scenarios
- Pytest fixtures
- Temporary test directories using `tmp_path`
- Mocking dependencies using `unittest.mock`
- Monkeypatching user input
- Capturing console output using `capsys`
- Assertions
- Code coverage measurement

### Test Results

The project currently includes 15 automated tests covering:

- Adding valid job applications.
- Validating required fields.
- Viewing job applications.
- Searching by company name.
- Handling unsuccessful searches.
- Updating job application status.
- Handling invalid and nonexistent job IDs.
- Deleting job applications.
- Cancelling deletion.
- Saving and loading JSON data.
- Handling missing JSON files.
- Testing operations with mocked storage dependencies.

The latest measured coverage before adding the mocked test was:

| Module | Coverage |
|---|---:|
| `job_operations.py` | 91% |
| `job_storage.py` | 73% |
| **Overall** | **87%** |

Coverage can change as additional tests are added.

## Concepts Practiced

### Python Fundamentals
- Variables and data types
- Lists and dictionaries
- Loops and conditional statements
- Functions and methods
- Exception handling
- File handling
- JSON serialization and deserialization
- List comprehensions and generator expressions

### Object-Oriented Programming
- Classes and objects
- Constructors (`__init__`)
- Instance attributes and methods
- Composition
- Dependency injection
- Separation of concerns
- Modular programming

### Software Development and Testing
- CRUD operations
- Unit testing with pytest
- Fixtures and assertions
- Mocking and monkeypatching
- Positive and negative testing
- Test coverage
- Git and GitHub
- Python virtual environments
- Dependency management using requirements.txt

## Future Enhancements

Potential improvements include:

- Integrating an external job-search API.
- Adding database support using SQLite or PostgreSQL.
- Implementing a graphical user interface or web application.
- Adding job application deadlines and interview reminders.
- Building an AI-powered job-search assistant.

---

**Project Status:** Completed foundational Python development, modular application architecture, CRUD functionality, JSON persistence, and automated unit testing.