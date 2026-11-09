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

        company = input("Enter company name: ")
        role = input("Enter job role: ")
        location = input("Enter location: ")
        status = input("Enter application status: ")

        job = {
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
        for index, job in enumerate(self.jobs_data, start=1):
            print(f"\nJob #{index}")
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
            print(f"\nJob #{index}")
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

        company = input("Enter company name: ").strip().lower()

        matching_jobs = [
            job for job in self.jobs_data if job["company"].lower() == company
        ]

        if not matching_jobs:
            print("\nJob not found.")
            return

        if len(matching_jobs) > 1:
            print("Multiple jobs found. Please use a unique company name.")
            return

        job = matching_jobs[0]

        print("Current status:", job["status"])

        new_status = input("Enter new status: ").strip()

        if not new_status:
            print("Status cannot be empty.")
            return

        job["status"] = new_status

        self.save_jobs()

        print("\nJob status updated successfully!")

    """Delete a job application."""
    def delete_job(self):
        self.load_jobs()

        if not self.jobs_data:
            print("\nNo job applications available.")
            return

        company = input("Enter company name to delete: ").strip().lower()

        matching_jobs = [
            job for job in self.jobs_data if job["company"].lower() == company
        ]

        if not matching_jobs:
            print("\nJob not found.")
            return

        if len(matching_jobs) > 1:
            print("Multiple jobs found. Please use a unique company name.")
            return

        self.jobs_data.remove(matching_jobs[0])

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
