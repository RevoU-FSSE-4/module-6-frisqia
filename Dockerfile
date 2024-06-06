
# use new image python as base image
FROM python:latest

# Set environment variable PYTHONUNBUFFERED sehingga output Python to print in the terminal without buffering
ENV PYTHONUNBUFFERED=1

# create directory app in Docker container
RUN mkdir /app

# Set working directory ke direktori app
WORKDIR /app

# copy all file from directory project app in docker container
COPY . /app

# Instal dependensi wich needed
RUN pip install -r requirements.txt

# Expose port 5000
EXPOSE 5000

# Run Flask when container to be start
CMD ["python", "app.py"]
