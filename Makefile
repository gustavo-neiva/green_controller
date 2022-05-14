init:
	pip install -r requirements.txt

run:
	nohup python -m green_controller &

stop:
	python3 green_controller/app.py