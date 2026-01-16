# API NOTES

# Request Methods:
# GET    - Read data from the server
# POST   - Create new data on the server
# PUT    - Update existing data on the server
# DELETE - Remove data from the server

# CRUD Operations: RESTful APIs use these methods to perform CRUD operations:
# Create (POST)
# Read (GET)
# Update (PUT)
# Delete (DELETE)

# Endpoints:
# /users         - Endpoint to manage users
# /users/{id}    - Endpoint to manage a specific user by ID
# /posts         - Endpoint to manage posts
# /posts/{id}    - Endpoint to manage a specific post by ID

# Status Codes:
# 200 - OK: The request was successful.
# 201 - Created: The resource was successfully created.
# 400 - Bad Request: The server could not understand the request due to invalid syntax.
# 404 - Not Found: The requested resource was not found on the server.
# 500 - Internal Server Error: The server encountered an unexpected condition that prevented it from fulfilling the request.

# Example Payloads:
# Creating a User (POST /users):
# {
#     "name": "John Doe",
#     "email": "jdoe@ex.com",   
#     "password": "password123"
# }

# Updating a User (PUT /users/{id}):
# {
#     "name": "John Doe",
#     "email": "jdoe@ex.com",   
#     "password": "password123"
# }

# REQUEST AND RESPONSE CYCLE Understanding

# Most asked questions:
# 1. What is a request-response cycle?
# A request-response cycle is the process by which a client (like a web browser) sends a request to a server, and the server processes that request and sends back a response. This cycle is fundamental to how web applications function.

# 2. How do APIs fit into this cycle?
# APIs (Application Programming Interfaces) are sets of rules that allow different software applications to communicate with
# each other. In the context of web applications, APIs define how clients can request data or services from a server and how the server should respond.


# 3. What are the common HTTP methods used in APIs?
# The most common HTTP methods used in APIs are GET (to retrieve data), POST (to create new data), PUT (to update existing data), and DELETE (to remove data).  
