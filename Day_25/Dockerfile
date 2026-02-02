# This is a sample Dockerfile for a simple web application
FROM python:3.9-slim
# FROM <language>:<version>-<variant>
# Example: FROM node:18-alpine
# Example: FROM openjdk:11-jre-slim

WORKDIR /app
# All commands now run in /app

COPY requirements.txt . 
RUN pip install --no-cache-dir -r requirements.txt
# Copy the dependencies file and install dependencies
# Docker caches layers-dependencies change less often than code
# If it's installed via pip/npm-> it belongs in a dependencies file

COPY . .
# Cpy only what the app needs to run - app file, models, configs, etc.

EXPOSE 5000
# Document the port the app runs on
# EXPOSE ≠ OPEN PORT 
# It's documentation for humans + tools

CMD ["python", "app.py"]
# CMD ["<runtime>", "<entry_file>"]
# Example: CMD ["node", "server.js"]
# Example: CMD ["java", "-jar", "app.jar"]
# Example: CMD ["npm", "start"]


# 1. Build the image: (recipe)
#    docker build -t my-web-app .
# Explanation:
#    docker build -t <image_name> .


# 2. Run a container from the image: (Actual cake)
#    docker run -p 5000:5000 my-web-app
# Explanation:
#    docker run -p <host_port>:<container_port> <image_name>