# Определение переменных
DOCKER_COMPOSE_FILE=./docker-compose.yml
PROJECT_DIR=./graphit-group-website


# Запуск окружения
up-deps:
	docker-compose -f $(DOCKER_COMPOSE_FILE) up -d

# Остановка окружения
down-deps:
	docker-compose -f $(DOCKER_COMPOSE_FILE) down

# Просмотр логов
logs:
	docker-compose -f $(DOCKER_COMPOSE_FILE) logs

# Просмотр процессов
ps:
	docker-compose -f $(DOCKER_COMPOSE_FILE) ps

# Выполнение миграций
migrate:
	cd $(PROJECT_DIR) && python manage.py makemigrations && python manage.py migrate

# Создание суперпользователя
createsuperuser:
	cd $(PROJECT_DIR) && python manage.py createsuperuser

# Запуск сервера разработки
runserver:
	cd $(PROJECT_DIR) && python manage.py runserver

# Запуск тестов
test:
	cd $(PROJECT_DIR) && python manage.py test

# Запуск всего: зависимостей и сервера
up: up-deps migrate runserver

# Остановка всего: сервера и зависимостей
down: down-deps

# Линтеры
pylint:
	pylint --load-plugins pylint_django graphit-group-website/

flake8:
	flake8 graphit-group-website/

# Помощь
help:
	@echo "Available commands:"
	@echo "  up-deps           Start the docker dependencies (Postgres, MinIO)"
	@echo "  down-deps         Stop the docker dependencies"
	@echo "  logs              View logs from docker containers"
	@echo "  migrate           Run Django migrations"
	@echo "  createsuperuser   Create a Django superuser"
	@echo "  runserver         Start the Django development server"
	@echo "  test              Run Django tests"
	@echo "  up                Start the full environment (dependencies + server)"
	@echo "  down              Stop the full environment"
	@echo "  help              Display this help message"