.PHONY: install run test init clean docker-build docker-run docker-stop docker-test

# Variables
VENV = venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

# Create virtual environment and install dependencies
install:
	python3.9 -m venv $(VENV)
	$(PIP) install -r requirements.txt

# Run the application
run:
	$(PYTHON) run.py

# Initialize database with sample data
init:
	$(PYTHON) init_db.py

# Run tests
test:
	$(PYTHON) -m pytest

# Run tests with verbose output
test-v:
	$(PYTHON) -m pytest -v

# Clean up environment
clean:
	rm -f foodbook.db
	rm -f test.db

# Docker commands
docker-build:
	docker-compose build

docker-run:
	docker-compose up -d

docker-stop:
	docker-compose down

docker-test:
	docker-compose exec foodbook python -m pytest

# Help
help:
	@echo "Available commands:"
	@echo "  make install     - Create virtual environment and install dependencies"
	@echo "  make run         - Run the application"
	@echo "  make init        - Initialize database with sample data"
	@echo "  make test        - Run tests"
	@echo "  make test-v      - Run tests with verbose output"
	@echo "  make clean       - Clean up database files"
	@echo "  make docker-build - Build the Docker image"
	@echo "  make docker-run   - Start services with Docker Compose"
	@echo "  make docker-stop  - Stop and remove Docker containers"
	@echo "  make docker-test  - Run tests in Docker container" 