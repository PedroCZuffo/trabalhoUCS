import os
import django
from django.contrib.auth import get_user_model
import django.core
import django.core.exceptions

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'trabalhoUCS.settings')
django.setup()

User = get_user_model()
username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
email = os.environ.get('DJANGO_SUPERUSER_EMAIL')
password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')

try:
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f'Superuser {username} created')
except Exception as _:
    print(f'Superuser {username} already exists')
