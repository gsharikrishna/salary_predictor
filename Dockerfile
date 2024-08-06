# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install system dependencies and any necessary build tools
RUN apt-get update && \
    apt-get install -y build-essential && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir django && \
    pip install --no-cache-dir scikit-learn && \
    pip install --no-cache-dir pandas && \
    pip install --no-cache-dir joblib && \
    pip install --no-cache-dir numpy

# Expose port 8000 for the Django app
EXPOSE 8000

# Define environment variable
ENV PYTHONUNBUFFERED=1

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
