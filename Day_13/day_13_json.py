# JSON
# JavaScript Object Notation

# Data types supported by JSON:
# - Strings
# - Numbers
# - Objects (key-value pairs)
# - Arrays (ordered list of values)
# - Booleans
# - Null

# JSON syntax rules:
# - Data is in name/value pairs
# - Data is separated by commas
# - Uses double quotes for strings and property names

import json
import os

filename = "student_db.json"

# The data (Python dictionary)
student_data = {
    "id" : 101,
    "name" : "John Doe",
    "marks" : [85, 90, 78],
    "is_active" : True
}

# Save data to a JSON file
print(f"Saving data to {filename}...")
with open(filename, 'w') as json_file:
    json.dump(student_data, json_file, indent=4)
print("Data saved successfully.")

# Simulate restarting the program
print("\nSimulating program restart...\n")
student_data = None

# Read data from the JSON file
if os.path.exists(filename):
    print(f"Loading data from {filename}...")
    with open(filename, 'r') as file:
        loaded_data = json.load(file)
    print("Data loaded successfully.")
    print(f" Type: {type(loaded_data)}")

    # Update the data
    print("\n Updating student data...")
    loaded_data['marks'].append(95)  # Adding a new mark

    # Save it back to the JSON file
    with open(filename, 'w') as json_file:
        json.dump(loaded_data, json_file, indent=4)
    print("Data updated and saved successfully.")
else:
    print(f"File {filename} does not exist.")