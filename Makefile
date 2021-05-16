.ONESHELL:

.PHONY: clean setup tests run all

clean:
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.log' -delete

setup:
	python3 -m venv venv; \
	. venv/bin/activate; \
	pip3 install -r requirements.txt;

tests:
	. venv/bin/activate; \
	python3 manage.py test

run:
	. venv/bin/activate; \
	python3 manage.py run

db:
	python3 manage.py db init; \
	python3 manage.py db migrate --message 'initial database migration'; \
	python3 manage.py db upgrade

all: clean setup tests db run 
