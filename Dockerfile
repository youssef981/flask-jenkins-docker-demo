# Use the official Python image
FROM python:3.11-alpine

# Set the working directory
WORKDIR /app

# Copy only the requirements file to avoid caching issues
COPY requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the current directory contents into the container
COPY . .

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "app.py"]