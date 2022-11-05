run:
	poetry run uvicorn api.main:app --reload
test:
	poetry run pytest