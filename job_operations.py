import json

class JobOperations:

    def __init__(self, job_storage):
        self.job_storage = job_storage

    def add_job(self):
        """Add a new job application."""
        jobs_data = self.job_storage.load_jobs()

        # Generate the next available ID
        next_id = max((job["id"] for job in jobs_data), default=0) + 1

        company = input("Enter company name: ").strip()
        role = input("Enter job role: ").strip()
        location = input("Enter location: ").strip()
        status = input("Enter application status: ").strip()

        # Validate required fields
        if not company or not role or not location or not status:
            print("\nAll fields are required. Job was not added.")
            return

        job = {
            "id": next_id,
            "company": company,
            "role": role,
            "location": location,
            "status": status
        }

        jobs_data.append(job)

        self.job_storage.save_jobs(jobs_data)

        print("\nJob application added successfully!")

    def view_jobs(self):
        """Display all job applications."""
        jobs_data = self.job_storage.load_jobs()

        if not jobs_data:
            print("\nNo job applications found.")
            return

        print("\n===== JOB APPLICATIONS =====")
        for job in jobs_data:
            print("\nJob #:", job["id"])
            print("Company:", job["company"])
            print("Role:", job["role"])
            print("Location:", job["location"])
            print("Status:", job["status"])

    def search_jobs(self):
        """Search job applications by company name."""
        jobs_data = self.job_storage.load_jobs()

        search_company = input("Enter company name to search: ").strip().lower()

        found_jobs = []

        for job in jobs_data:
            if search_company in job["company"].lower():
                found_jobs.append(job)

        if not found_jobs:
            print("\nNo matching jobs found.")
            return

        print("\n===== SEARCH RESULTS =====")
        for index, job in enumerate(found_jobs, start=1):
            print("Job #:", job["id"])
            print("Company:", job["company"])
            print("Role:", job["role"])
            print("Location:", job["location"])
            print("Status:", job["status"])

    def update_job_status(self):
        """Update the status of a job application."""
        jobs_data = self.job_storage.load_jobs()

        if not jobs_data:
            print("\nNo job applications available.")
            return

        print("\n===== AVAILABLE JOBS =====")

        for job in jobs_data:
            print(
                f"ID: {job['id']} | "
                f"Company: {job['company']} | "
                f"Role: {job['role']} | "
                f"Status: {job['status']}"
            )

        try:
            job_id = int(input("\nEnter Job ID to update: "))

        except ValueError:
            print("Invalid ID. Please enter a number.")
            return

        matching_job = next(
            (job for job in jobs_data if job["id"] == job_id), None
        )

        if matching_job is None:
            print("\nJob ID not found.")
            return

        print("\nCompany:", matching_job["company"])
        print("Role:", matching_job["role"])
        print("Current status:", matching_job["status"])

        new_status = input("Enter new status: ").strip()

        if not new_status:
            print("Status cannot be empty.")
            return

        matching_job["status"] = new_status

        self.job_storage.save_jobs(jobs_data)

        print("\nJob status updated successfully!")

    def delete_job(self):
        """Delete a job application."""
        jobs_data = self.job_storage.load_jobs()

        if not jobs_data:
            print("\nNo job applications available.")
            return

        print("\n===== AVAILABLE JOBS =====")

        for job in jobs_data:
            print(
                f"ID: {job['id']} | "
                f"Company: {job['company']} | "
                f"Role: {job['role']} | "
                f"Status: {job['status']}"
            )

        try:
            job_id = int(input("\nEnter Job ID to delete: "))

        except ValueError:
            print("Invalid ID. Please enter a number.")
            return

        matching_job = next(
            (job for job in jobs_data if job["id"] == job_id), None
        )

        if matching_job is None:
            print("\nJob ID not found.")
            return

        print("\nSelected job:")
        print("Company:", matching_job["company"])
        print("Role:", matching_job["role"])

        confirmation = input("Are you sure you want to delete? (yes/no): ").strip()
        if confirmation.strip().lower() != "yes":
            print("\nDeletion cancelled.")
            return

        jobs_data.remove(matching_job)

        self.job_storage.save_jobs(jobs_data)

        print("\nJob deleted successfully!")

