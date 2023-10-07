FROM python:3.9-slim

MAINTAINER Anatoly Rozhkov <anatoly.rozhkov1998@gmail.com>

ENV PYTHONUNBUFFERED 1

# Create the /app/project/tests directory structure inside the container
RUN mkdir -p /app/project/tests

# Copy the requirements file to /app/project/tests/requirements.txt
COPY project/tests/requirements.txt /app/project/tests/requirements.txt

# Set the working directory to /app
WORKDIR /app

# Copy the entire project directory to /app/project
COPY project/ /app/project

# Set the PYTHONPATH environment variable
ENV PYTHONPATH="/app/project:${PYTHONPATH}"


# Install dependencies and configure the environment
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apt-get update && \
    /py/bin/pip install -r /app/project/tests/requirements.txt

ENV PATH="/py/bin:$PATH"