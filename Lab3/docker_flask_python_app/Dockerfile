# Use the official Python image as the base image
FROM python:3.11-slim

# Set the working directory inside the container
zzzWORKDIR /app

# Copy the application files to the container
# COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that Flask will use
EXPOSE 4567

# Define the command to run the Flask application
RRRCMD ["python", "app.py"]
asCMD ["python", "app.py"]
