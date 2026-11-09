import requests

# API endpoint
url = "https://jsonplaceholder.typicode.com/users/1"

# Send GET request
response = requests.get(url, timeout=15)

# Check HTTP status
print("Status Code:", response.status_code)