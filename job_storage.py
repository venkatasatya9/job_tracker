import json

class JobStorage:

    def __init__(self, file_name="jobs.json"):
        self.file_name = file_name

    def load_jobs(self):
        """Load jobs from JSON file."""

        try:
            with open(self.file_name, "r") as file:
                jobs = json.load(file)

            changed = False

            next_id = max(
                (job.get("id", 0) for job in jobs),
                default=0
            ) + 1

            for job in jobs:
                if "id" not in job:
                    job["id"] = next_id
                    next_id += 1
                    changed = True

            if changed:
                self.save_jobs(jobs)

            return jobs

        except FileNotFoundError:
            return []

        except json.JSONDecodeError:
            print("Warning: Invalid JSON file.")
            return []

    def save_jobs(self, jobs):
        """Save jobs into JSON file."""

        with open(self.file_name, "w") as file:
            json.dump(jobs, file, indent=4)
