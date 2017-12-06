# Using official python runtime base image
FROM docker:latest

RUN apk upgrade --no-cache \
  && apk add --no-cache \
    musl \
    build-base \
    python3 \
    python3-dev \
    postgresql-dev \
    bash \
    git \
  && pip3 install --no-cache-dir --upgrade pip \
  && rm -rf /var/cache/* \
  && rm -rf /root/.cache/*

# Set the application directory
WORKDIR /tests

# Install our requirements.txt
ADD requirements.txt /tests/requirements.txt
RUN pip3 install -r requirements.txt

# Copy our code from the current folder to /app inside the container
ADD . /tests

# Define our command to be run when launching the container.
ENTRYPOINT ["ash", "run.sh"]
