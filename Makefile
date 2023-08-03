install:
		poetry install

gendiff:
		poetry run gendiff

build:
		poetry build

publish:
		poetry publish --dry-run

package-install:
		python3 -m pip install --user dist/hexlet_code-0.1.0-py3-none-any.whl

package-reinstall:
		python3 -m pip install . --force-reinstall

lint:
		poetry run flake8 gendiff
