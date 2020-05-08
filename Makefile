install:
	@poetry install

build:
	@poetry build

publish:
	@poetry publish -r tatoxer_gendiff

lint:
	@poetry run flake8 gendiff

pytest:
	@poetry run pytest --cov=gendiff --cov-report xml gendiff/tests/fixtures/
