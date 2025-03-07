PHONY: test
test:
	@echo 'tests started...'
	@pytest . -v


PHONY:  check
check: test
	echo 'tests started...'
	black .
	isort .
	flake8 .