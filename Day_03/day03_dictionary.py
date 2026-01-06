# DICTIONARIES
# A dictionary is a collection which is unordered, changeable and indexed.
# In Python dictionaries are written with curly brackets, and they have keys and values.

# Creating a dictionary
student = {
    "name": "John",
    "age": 21,
    "courses": ["Math", "CompSci"]
}
print(student)

# Accessing values
print(student["name"])  # Output: John
print(student.get("age"))  # Output: 21
print(student.get("gender"))  # Output: None (key does not exist)
print(student.get("gender", "Not Specified"))  # Output: Not Specified

# Adding or updating values
student["phone"] = "555-5555"  # Adding a new key-value pair
student["name"] = "Jane"  # Updating an existing key

student.update({"age": 22, "address": "123 Main St"})  # Updating multiple key-value pairs
print(student)

# Removing values
del student["age"]  # Remove key-value pair by key
phone = student.pop("phone")  # Remove key-value pair and return the value
print(f"Removed phone number: {phone}")
print(student)

print(len(student))  # Output: Number of key-value pairs in the dictionary
print(student.values())  # Output: dict_values(['Jane', ['Math', 'CompSci'], '123 Main St'])
print(student.keys())  # Output: dict_keys(['name', 'courses', 'address'])
print(student.items())  # Output: dict_items([('name', 'Jane'), ('courses', ['Math', 'CompSci']), ('address', '123 Main St')])

# Looping through a dictionary
for key, value in student.items():
    print(key, value)