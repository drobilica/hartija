#comment

.PHONY: up down clean env

env:
	pipenv shell

run:
	pipenv run flask run

install:
	pipenv update


down:
	docker-compose down

up:
	docker-compose up -d

clean: down
	docker container prune -f && docker volume prune -f && docker image rm hartija_api

build:
	docker-compose build


