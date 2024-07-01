# Mention the python version for base image
FROM python:3.9

# Prevents docker from buffereing the output and displays it in the console
ENV PYTHONNUNBUFFERED 1

# Mention the working directory in the docker container
WORKDIR /app

# Copy the requirement.txt file to the container's app directory
COPY requirements.txt /app/requirements.txt

# Install all the dependencies on the container
RUN pip install -r requirements.txt

# Copy all the contents of the current working directory to app
COPY . /app

# Container will use this command to run the django development server
CMD python manage.py runserver 0.0.0.0:8000