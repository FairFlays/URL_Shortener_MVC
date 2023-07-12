style:
	isort src/
	black src/

lint:
	pflake8 src/
	mypy src/
