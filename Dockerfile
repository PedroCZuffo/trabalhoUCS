# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install Django and other dependencies
RUN pip install django djangorestframework django-jazzmin pillow

# Copy the create_superuser.py script
COPY create_superuser.py /usr/src/app/

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run the Django server
CMD ["sh", "-c", "python manage.py makemigrations && python manage.py migrate && python create_superuser.py && python manage.py runserver 0.0.0.0:8000"]
