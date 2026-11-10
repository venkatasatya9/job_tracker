import json

class Jobs:

    def __init__(self):
        self.FILE_NAME = "jobs.json"
        self.jobs_data = []

    """Load job applications from JSON file."""
    def load_jobs(self):
        try:
            with open(self.FILE_NAME, 'r') as file:
                self.jobs_data = json.load(file)

            changed = False

            next_id = max((job.get("id", 0) for job in self.jobs_data), default=0) + 1

            for job in self.jobs_data:
                if "id" not in job:
                    job["id"] = next_id
                    next_id += 1
                    changed = True

            # Save the file only if IDs were added
            if changed:
                self.save_jobs()

        except FileNotFoundError:
            self.jobs_data = []

        except json.JSONDecodeError:
            print("Warning: Invalid JSON file. Starting with an empty list.")
            self.jobs_data = []

    """Save job applications into JSON file."""
    def save_jobs(self):
        with open(self.FILE_NAME, 'w') as file:
            json.dump(self.jobs_data, file, indent=4)

    """Add a new job application."""
    def add_job(self):
        self.load_jobs()

        # Generate the next available ID
        next_id = max((job["id"] for job in self.jobs_data), default=0) + 1

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

        self.jobs_data.append(job)

        self.save_jobs()

        print("\nJob application added successfully!")

    """Display all job applications."""
    def view_jobs(self):
        self.load_jobs()

        if not self.jobs_data:
            print("\nNo job applications found.")
            return

        print("\n===== JOB APPLICATIONS =====")
        for job in self.jobs_data:
            print("\nJob #:", job["id"])
            print("Company:", job["company"])
            print("Role:", job["role"])
            print("Location:", job["location"])
            print("Status:", job["status"])

    """Search job applications by company name."""
    def search_jobs(self):
        self.load_jobs()

        search_company = input("Enter company name to search: ").strip().lower()

        found_jobs = []

        for job in self.jobs_data:
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

    """Update the status of a job application."""
    def update_job_status(self):
        self.load_jobs()

        if not self.jobs_data:
            print("\nNo job applications available.")
            return

        print("\n===== AVAILABLE JOBS =====")

        for job in self.jobs_data:
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
            (job for job in self.jobs_data if job["id"] == job_id), None
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

        self.save_jobs()

        print("\nJob status updated successfully!")

    """Delete a job application."""
    def delete_job(self):
        self.load_jobs()

        if not self.jobs_data:
            print("\nNo job applications available.")
            return

        print("\n===== AVAILABLE JOBS =====")

        for job in self.jobs_data:
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
            (job for job in self.jobs_data if job["id"] == job_id), None
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

        self.jobs_data.remove(matching_job)

        self.save_jobs()

        print("\nJob deleted successfully!")

    def run(self):
        while True:
            print("\n===== JOB SEARCH TRACKER =====")
            print("1. Add Job")
            print("2. View Jobs")
            print("3. Search Jobs")
            print("4. Update Job Status")
            print("5. Delete Job")
            print("6. Exit")

            choice = input("\nEnter your choice: ")

            if choice == "1":
                self.add_job()

            elif choice == "2":
                self.view_jobs()

            elif choice == "3":
                self.search_jobs()

            elif choice == "4":
                self.update_job_status()

            elif choice == "5":
                self.delete_job()

            elif choice == "6":
                print("Thank you for using Job Search Tracker!")
                break

            else:
                print("Invalid choice. Please try again.")

if __name__ == '__main__':
    my_jobs = Jobs()
    my_jobs.run()
