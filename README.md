# lawyer site
# Activate
    python3 -m venv venv
    source venv/bin/activate
    python3 -m pip install --upgrade pip
___

# Installation Django
    pip install django==4.1.5 # Stable 3.2 # Next stable 4.2
    python -m pip install Pillow # For image

    django-admin startproject config . # Create directory 'config'
    python manage.py migrate
    python manage.py makemigrations
    python manage.py createsuperuser #user/user ))
    python manage.py runserver #Starting development server

    django-admin startapp bin

    python manage.py migrate --run-syncdb
___
# dotenv    
    pip install python-dotenv
___
# for singleton model https://pypi.org/project/django-solo/

    pip install django-solo
___
# Save to requirements.txt

    pip freeze > requirements.txt



