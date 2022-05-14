install:
	pip install -r requirements.txt

run:
	python -m green_controller

stop:
	pkill -f green_controller