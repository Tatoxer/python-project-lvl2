install:
	@poetry install

build:
	@poetry build

publish:
	@poetry publish -r tatoxer_gendiff

lint:
	@poetry run flake8 gendiff

test:
	@poetry run pytest -vv --cov=gendiff --cov-report xml tests
