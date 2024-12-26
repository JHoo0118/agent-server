start:
	python main.py

generate:
	python3 -m prisma generate

lint:
	poetry run isort . & poetry run black . & poetry run flake8

.PHONY: start generate lint 