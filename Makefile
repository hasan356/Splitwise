build:
	pip3 install -r requirements.txt
	python3 manage.py makemigrations
	python3 manage.py migrate

run:
	python3 manage.py runserver