# Use new image python as base image
FROM python:latest

# Set environment variable PYTHONUNBUFFERED so output Python to print in the terminal without buffering
ENV PYTHONUNBUFFERED=1

# Create directory app in Docker container
RUN mkdir /app

# Set working directory to directory app
WORKDIR /app

# Copy all files from directory project app in docker container
COPY . /app

# Install dependencies from Pipfile
RUN pip install pipenv
RUN pipenv install --system --deploy

# Expose port 5000
EXPOSE 5000

# Run Flask when container starts
CMD ["python", "app.py"]