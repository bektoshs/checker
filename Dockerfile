<<<<<<< HEAD
FROM python:3.10-slim
=======
# Use an official Python runtime as a parent image
FROM python:3.9
>>>>>>> 375d60c08931c550cdddbfb844fa7a8e041fd8f9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
<<<<<<< HEAD
WORKDIR /website_status

# Install dependencies
COPY requirements.txt /website_status/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install gunicorn

# Copy project
COPY . /website_status/

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose the port your app runs on
EXPOSE 8080

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]

=======
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Copy project
COPY . /code/

# Command to run the application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "website_status.wsgi:application"]
>>>>>>> 375d60c08931c550cdddbfb844fa7a8e041fd8f9
