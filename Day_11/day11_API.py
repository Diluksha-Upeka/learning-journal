# DAY 11: HTTP API SIMULATION
# API = Application Programming Interface

import json

class MockServer:
    def __init__(self):
        # This is our "Database"
        self.users = {
            1: "Diluksha",
            2: "Saman"
        }

    def handle_request(self, method, endpoint, payload=None):
        print(f"REQUEST: {method} {endpoint} | Data: {payload}")
        
        # 1. ROUTING (Checking the endpoint)
        if endpoint == "/users":
            
            # 2. HANDLING METHODS
            if method == "GET":
                return {"status": 200, "body": self.users}
            
            elif method == "POST":
                # Creating a new user
                new_id = len(self.users) + 1
                self.users[new_id] = payload
                return {"status": 201, "body": {"msg": "Created", "id": new_id}}
        
        elif endpoint.startswith("/users/"):
            # Extract ID from /users/1
            try:
                user_id = int(endpoint.split("/")[-1])
                
                if method == "GET":
                    if user_id in self.users:
                        return {"status": 200, "body": self.users[user_id]}
                    else:
                        return {"status": 404, "body": {"error": "User Not Found"}}
                
                elif method == "PUT":
                    # Update existing user
                    if user_id in self.users:
                        self.users[user_id] = payload
                        return {"status": 200, "body": {"msg": "Updated", "id": user_id, "name": payload}}
                    else:
                        return {"status": 404, "body": {"error": "User Not Found"}}
                        
            except:
                return {"status": 400, "body": {"error": "Bad Request"}}

        # Default: 404 Not Found
        return {"status": 404, "body": {"error": "Endpoint Not Found"}}
    

# SIMULATING THE CLIENT (The Browser)

server = MockServer()

# SCENARIO 1: Get all users (GET)
# READ 
# response = server.handle_request("GET", "/users")
# print(f"RESPONSE: {response}")

# # SCENARIO 2: Create a new user (POST)
# CREATE
response = server.handle_request("POST", "/users", payload="Kamal")
print(f"RESPONSE: {response}")

response = server.handle_request("GET", "/users")
print(f"RESPONSE: {response}")

# # SCENARIO 2.1: Update an existing user (PUT)
# UPDATE
response = server.handle_request("PUT", "/users/2", payload="Saman Updated")
print(f"RESPONSE: {response}")

response = server.handle_request("GET", "/users")
print(f"RESPONSE: {response}")

# # SCENARIO 3: Try to find a user that doesn't exist (404 Error)
response = server.handle_request("GET", "/users/99")
print(f"RESPONSE: {response}")

# # SCENARIO 4: Get a specific user (GET)
response = server.handle_request("GET", "/users/1")
print(f"RESPONSE: {response}")

# # SCENARIO 5: Bad Request (Invalid ID)
response = server.handle_request("GET", "/users/abc")
print(f"RESPONSE: {response}")

# # SCENARIO 6: Invalid Endpoint
response = server.handle_request("GET", "/invalid")
print(f"RESPONSE: {response}")