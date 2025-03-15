PHONY: test
test:
	@echo 'tests started...'
	@set PYTHONPATH=. && python -m pytest -v -s


PHONY:  check
check: test
	echo 'tests started...'
	black .
	isort .
	flake8 .