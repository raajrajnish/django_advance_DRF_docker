# STEP 1. Define Docker Image to work with (mandatory)
# python:latest - we will pick latest tag image from dockerhub
FROM python:3.7-alpine
# optional step
MAINTAINER raajrajnish

# Step 2. Setting env as unbufferedmode hence it donot allows the python to buffer outputs
# hence simply print it, it is recommended to run pytho in unbuffered mode in docker container
ENV PYTHONUNBUFFERED 1

# Step 3. Install dependencies, first copy then install
COPY ./requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
      gcc libc-dev linux-headers postgresql-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

# Step 4. Create directory to keep our application source code in docker
RUN mkdir /app
# setting docker working directory
WORKDIR app
# copies local copy of app folder to docker app folder
COPY ./app /app

# Step 5. Setting user (not mandatory step but good to implement as it, enhance security aspect
# by not using root user which as all previlages but uses a user which has only application
# running previlages )
# because of an issue removing below lines
# https://stackoverflow.com/questions/56784492/docker-compose-permissionerror-errno-13-permission-denied-manage-py/56784562
# RUN useradd -u 8877 user
# USER user