# DAY 14: MINI PROJECT - SCHOOL API

from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__) # Starts a web server

# Store DB file next to this script (so it works no matter where you run it from)
BASE_DIR = os.path.dirname(__file__)
DB_FILE = os.path.join(BASE_DIR, "school_db.json")

student_data = {
    "id" : 101,
    "name" : "John Doe",
    "marks" : [85, 90, 78],
    "is_active" : True
}


def seed_db_if_empty():
    data = load_db()

    # Only seed once (so you don't overwrite real data)
    if data == {}:
        data["101"] = student_data
        save_db(data)


# HELPER: Load DB from file
# Returns a dictionary of students
def load_db():
    if not os.path.exists(DB_FILE):
        return {}  # Return empty dict if file doesn't exist
    with open(DB_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


# HELPER: Save DB to file
# data is a dictionary
def save_db(data):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


# ROUTE 1: Get All Students (GET)
@app.route("/students", methods=["GET"])
def get_students():
    data = load_db()
    return jsonify(data)  # Returns 200 OK automatically


# ROUTE 2: Add a Student (POST)
# Client sends JSON: {"name": "Diluksha", "age": 25}
@app.route("/students", methods=["POST"])
def add_student():
    # 1. Get data from the user
    new_student = request.json

    # 2. Validation (Simple "If" check)
    if not new_student or "name" not in new_student:
        return jsonify({"error": "Name is required"}), 400

    # 3. Load, Update, Save
    data = load_db()

    # Generate a simple ID (e.g., "101")
    new_id = str(len(data) + 101)
    data[new_id] = new_student

    save_db(data)

    return jsonify({"msg": "Student Added", "id": new_id}), 201


# ROUTE 3: Find Student by ID (GET) - O(1) Lookup!
@app.route("/students/<student_id>", methods=["GET"])
def get_one_student(student_id):
    data = load_db()

    # Dictionary Lookup is O(1) - Fast!
    if student_id in data:
        return jsonify(data[student_id])
    else:
        return jsonify({"error": "Student not found"}), 404


# Run the Flask app
if __name__ == "__main__":
    # Create an empty DB file if needed
    if not os.path.exists(DB_FILE):
        save_db({})

    # Add the default student the first time you run it
    seed_db_if_empty()

    print("School API is running on http://127.0.0.1:5000")
    app.run(debug=True)
