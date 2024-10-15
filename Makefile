venv:
		python -m pip install virtualenv && python -m venv venv

install:
		python -m pip install -r requirements.txt

up:
		python manage.py runserver
