Use the official Python image as a base

FROM python:3.11-slim

Set the working directory in the container

WORKDIR /app

Copy the requirements file into the container

COPY requirements.txt .

Install the dependencies

RUN pip install --no-cache-dir -r requirements.txt

Copy the entire application code into the container

COPY . .

Set the environment variable for the port (optional, but good practice)

ENV PORT 8080

The command to start the application server

Gunicorn binds to 0.0.0.0 and uses the $PORT environment variable

app:app means "look for the application instance named 'app' in the file 'app.py'"

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app