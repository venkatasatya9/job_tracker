import json

try:
    with open("user_data.json", "r") as file:
        user_data = json.load(file)

    print("\nUser Information")
    print("----------------")
    print("Name:", user_data["name"])
    print("Username:", user_data["username"])
    print("Email:", user_data["email"])
    print("Phone:", user_data["phone"])
    print("Website:", user_data["website"])

except FileNotFoundError:
    print("Error: File not found.")

except ValueError:
    print("Error: Invalid JSON file.")