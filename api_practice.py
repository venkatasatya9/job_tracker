import requests
import json

# API endpoint
url = "https://jsonplaceholder.typicode.com/users/1"
# url = "https://jsonplaceholder.typicode.com/invalid_endpoint"

try:
    # Step 1: Make API request
    response = requests.get(url, timeout=15)

    # Step 2: Validate HTTP response
    response.raise_for_status()

    # Step 3: Convert API response into Python dictionary
    user_data = response.json()

    # Step 4: Save API response into JSON file
    with open("user_data.json", "w") as file:
        json.dump(user_data, file, indent=4)

    print("API data retrieved successfully!")
    print("API response saved into user_data.json")

    # Step 5: Display selected information
    print("\nUser Information")
    print("----------------")
    print("Name:", user_data["name"])
    print("Email:", user_data["email"])
    print("City:", user_data["address"]["city"])

except requests.exceptions.Timeout:
    print("Error: API request timed out.")

except requests.exceptions.ConnectionError:
    print("Error: Unable to connect to the server.")

except requests.exceptions.HTTPError as error:
    print("HTTP Error:", error)

except requests.exceptions.RequestException as error:
    print("Request Error:", error)

except ValueError:
    print("Error: Invalid JSON response.")

except OSError as error:
    print("File Error:", error)
