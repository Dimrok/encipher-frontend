# Using official python runtime base image
FROM python:3.6.3-alpine3.6

# Set the application directory
WORKDIR /app

# Install our requirements.txt
ADD requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt

# Copy our code from the current folder to /app inside the container
ADD . /app

# Make port 80 available for links and/or publish
EXPOSE 80

VOLUME /var/run/docker.sock

# Define our command to be run when launching the container
CMD ["gunicorn", "app:app", "-b", "0.0.0.0:80", "--log-file", "/tmp/app.log", "--access-logfile", "/tmp/access.log", "--workers", "4", "--keep-alive", "0"]
