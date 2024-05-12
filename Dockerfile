# Use an official Python runtime as a parent image
FROM python:3.12.3

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Make port available to the world outside this container
EXPOSE 8080

# Define environment variable(if any)
#ENV NAME World

# Run app.py when the container launches
CMD ["python3", "app.py"]
