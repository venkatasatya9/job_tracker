from job_storage import JobStorage
from job_operations import JobOperations

class JobTracker:

    def __init__(self):
        self.FILE_NAME = "jobs.json"
        self.jobs_data = []
        self.job_storage = JobStorage(self.FILE_NAME)
        self.job_operations = JobOperations(self.job_storage)

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
                self.job_operations.add_job()

            elif choice == "2":
                self.job_operations.view_jobs()

            elif choice == "3":
                self.job_operations.search_jobs()

            elif choice == "4":
                self.job_operations.update_job_status()

            elif choice == "5":
                self.job_operations.delete_job()

            elif choice == "6":
                print("Thank you for using Job Search Tracker!")
                break

            else:
                print("Invalid choice. Please try again.")

if __name__ == '__main__':
    tracker = JobTracker()
    tracker.run()
