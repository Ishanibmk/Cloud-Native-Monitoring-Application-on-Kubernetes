# This Dockerfile is for a Flask application.
# It uses the official Python 3.9 slim image as a base image.
# The application is copied into the container, and the required Python packages are installed.
FROM python:3.9-slim-buster

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
# This includes the Flask application and the requirements.txt file
COPY requirements.txt . 

# Install any needed packages specified in requirements.txt
# The --no-cache-dir option is used to prevent caching of the package indexs
# This helps to keep the image size smaller
RUN pip install --no-cache-dir -r requirements.txt 

# Copy the rest of the application code into the container at /app
# This includes the Flask application code and any other necessary files
COPY . . 

# Set environment variables for Flask for the Docker container to run
ENV FLASK_RUN_HOST=0.0.0.0

# Set the Flask environment to development for debugging purposes with port 5000 i.e. the default port for Flask is my local host
EXPOSE 5000

# Set the command to run the Flask application when the container starts
#CMD [executable = "flask", paramter = "run"]
# This command will start the Flask development server
CMD ["flask", "run"] 


