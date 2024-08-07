# Use new image python as base image
FROM --platform=linux/arm64 python:3.12-slim

# Set environment variable PYTHONUNBUFFERED so output Python to print in the terminal without buffering
ENV PYTHONUNBUFFERED=1

# Create directory app in Docker container
RUN mkdir /app

# Set working directory to directory app
WORKDIR /app

# Copy all files from directory project app in docker container
COPY . /app
COPY Pipfile Pipfile.lock

# Install dependencies from Pipfile
RUN pip install -U pipenv
RUN pipenv install --deploy

# Expose port 5000
EXPOSE 8080

# Run Flask with Gunicorn when container starts
CMD ["pipenv", "run", "gunicorn", "-w", "4", "-b", "0.0.0.0:8080", "app:app"]
