install:
		poetry install

package-install:
		python3 -m pip install --user dist/hexlet_code-0.1.0-py3-none-any.whl

package-reinstall:
		python3 -m pip install . --force-reinstall

test:
		poetry run pytest

test-coverage:
		poetry run pytest --cov=gendiff --cov-report xml

lint:
		poetry run flake8 gendiff

selfcheck:
		poetry check

check: 
		selfcheck test lint

build:
		check
		poetry build

