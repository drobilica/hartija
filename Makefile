#comment

.PHONY: up down clean env

env:
	. env/bin/activate

down:
	docker-compose down

up:
	docker-compose up -d

clean: down
	docker container prune -f && docker volume prune -f && docker image rm suster_api

build:
	docker-compose build
