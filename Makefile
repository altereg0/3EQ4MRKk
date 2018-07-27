init:
	pip install -r requirements.txt

dev:
	pip install -r dev-requirements.txt

test:
	nosetests -vv tests
