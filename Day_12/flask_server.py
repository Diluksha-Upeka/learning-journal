from flask import Flask, jsonify

# Create the server object
app = Flask(__name__)

# ROUTE 1 - Home Route
# When user goes to http://localhost:5000/
@app.route("/")
def home():
    return "Welcome to the Home Page!"  

# ROUTE 2 - The API Route (Data)
# When user goes to http://localhost:5000/api
@app.route("/api")
def get_data():
    data = {
        "name": "Flask API",
        "version": "1.0",
        "description": "This is a simple Flask API"
    }
    return jsonify(data)  # Return data as JSON
    # jsonify() converts the dictionary to a JSON response


# Start the server
if __name__ == "__main__":
    app.run(debug=True)  # Run the server in debug mode for easier development
    # debug=True means the server will auto-reload on code changes and show detailed error messages