# Job Search Tracker

A command-line Python application for managing job applications. It stores application records in a JSON file so that information is preserved between sessions.

## Features

- **Add Job:** Add a job application with a unique ID, company, role, location, and application status.
- **View Jobs:** Display all saved job applications.
- **Search Jobs:** Search applications by company name.
- **Update Job Status:** Update an application using its unique Job ID.
- **Delete Job:** Delete a specific application using its Job ID, with a confirmation step.
- **Persistent Storage:** Save and load job applications using JSON.

## Technologies

- Python
- JSON
- Git and GitHub

## Project Structure

```text
taskmanager/
│
├── job_tracker.py       # Main Job Search Tracker application
├── jobs.json            # Local job application data (not committed)
├── README.md            # Project documentation
├── requirements.txt     # Python environment dependencies
└── .gitignore           # Files excluded from Git
```

## Requirements

- Python installed on your computer.
- No third-party packages are required to run the Job Search Tracker itself.

## How to Run

1. Clone or download this repository.
2. Open the project folder in a terminal.
3. (Optional) Create and activate a virtual environment:

   ```bash
   python -m venv venv
   ```

   Windows PowerShell:

   ```powershell
   venv\Scripts\activate
   ```

4. Run the application:

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

- `id`: Unique job application ID
- `company`: Company name
- `role`: Job title
- `location`: Job location
- `status`: Application status

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

**Note:** `jobs.json` contains personal application information. It is excluded from Git so that your private job-search data is not uploaded to the public repository.

## Concepts Practiced

- Python functions and modular programming
- Lists and dictionaries
- Loops and conditional statements
- Exception handling
- File handling
- JSON serialization and deserialization
- List comprehensions and generator expressions
- Searching and updating records
- CRUD operations
- Git and GitHub
- Python virtual environments
