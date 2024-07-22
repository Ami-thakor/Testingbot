# Use an official Python runtime as a parent image
FROM python:3.10.8-slim-buster

# Update and upgrade the system packages
RUN apt update && apt upgrade -y

# Install git
RUN apt install git -y

# Copy the requirements file into the container
COPY requirements.txt /requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r /requirements.txt

# Create and set the working directory
RUN mkdir /app
WORKDIR /app

# Copy the rest of the application code into the container
COPY . /app

# Run the bot script when the container launches
CMD ["python", "bot.py"]
