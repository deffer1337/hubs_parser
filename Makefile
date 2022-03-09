migrate:
	python src/manage.py migrate $(if $m, api $m,)

makemigrations:
	python src/manage.py makemigrations
	sudo chown -R ${USER} src/app/migrations/

createsuperuser:
	python src/manage.py createsuperuser

dev:
	python src/manage.py runserver localhost:8001

command:
	python src/manage.py ${c}

shell:
	python src/manage.py shell

debug:
	python src/manage.py debug

lint:
	isort .
	flake8 --config setup.cfg
	black --config pyproject.toml .

check_lint:
	isort --check --diff .
	flake8 --config setup.cfg
	black --check --config pyproject.toml .

build:
	sudo docker-compose build

run_hubs_parser:
	sudo docker-compose up hubs_parser
	sudo docker-compose up redis

down_hubs_parser:
	sudo docker-compose down hubs_parser
	sudo docker-compose down redis

web:
	sudo docker-compose up web

down_web:
	sudo docker-compose down web