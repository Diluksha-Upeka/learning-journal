# FLASK

# Create a virtual environment
# python -m venv venv

# Activate the virtual environment
# On Windows: venv\Scripts\activate

# Install Flask
# pip install Flask

from flask import Flask, redirect, url_for

app = Flask(__name__) # Create a Flask application instance

@app.route("/") # Define a route for the root URL
def home():     # Define a view function for the route
    return "Hello, Flask!"

@app.route("/<name>") # Define a route for the /user URL
def user(name):
    return f"User Page: {name}"

@app.route("/admin") # Define a route for redirection
def admin():
    return redirect(url_for("home")) # Redirect to the home page

if __name__ == "__main__": # Run the application only if this script is executed directly
    app.run()


# How to write a simple Flask application:
# 1. Import the Flask class from the flask module.
        # import Flask, redirect, url_for

# 2. Create a Flask application instance.   
        #    app = Flask(__name__)

# 3. Define routes using the @app.route() decorator.
        #    @app.route("/")
        #    def home():

# 4. Define view functions that return responses for each route.
        #    def home():
        #        return "Hello, Flask!"

# 5. Use app.run() to run the application.
        #    if __name__ == "__main__":
        #        app.run()