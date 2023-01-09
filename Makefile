install:
	pip install -r requirements.txt

dev:
	python -m green_controller

prod:
	gunicorn -w 1 -b 0.0.0.0:4000 green_controller.server:app

stop:
	pkill -f green_controller