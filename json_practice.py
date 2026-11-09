import json

# Python dictionary
job = {
    "company": "Google",
    "role": "Data Engineer",
    "location": "Atlanta",
    "skills": ["Python", "SQL", "Databricks"],
    "status": "Applied",
    "remote": True
}

# Write dictionary into a JSON file
with open('job.json', 'w') as file:
    json.dump(job, file, indent=4)

print("Job information saved successfully!")

# Read data from the JSON file
with open('job.json', 'r') as file:
    loaded_job = json.load(file)

# Display the complete dictionary
# print(loaded_job)

# Access individual values
print("Company:", loaded_job["company"])
print("Role:", loaded_job["role"])
print("Number of Skills:", len(loaded_job["skills"]))
print("Skills:")
for skill in loaded_job["skills"]:
    print(skill)
print("Application Status:", loaded_job["status"])


job_string = {
    "company": "Microsoft",
    "role": "Data Engineer",
    "status": "Interview"
}
print("\n=== JSON String ===")
# Convert Python dictionary into JSON string
json_string = json.dumps(job_string, indent=4)

print(json_string)

print("\n=== Python Dictionary ===")
# Convert JSON string back into Python dictionary
python_dict = json.loads(json_string)

print(python_dict)