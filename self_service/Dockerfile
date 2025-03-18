# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install required packages: yq for YAML processing, git for repo handling, and dependencies
RUN apt-get update && apt-get install -y yq git && \
    pip install gitpython

# Copy the Python script into the container
COPY self_service.py /app/self_service.py

# Set the default command to run the script
CMD ["python", "/app/self_service.py"]
