from .controller import Controller
from time import sleep
import threading
import signal
import logging
from apscheduler.schedulers.background import BackgroundScheduler
import threading

scheduler = BackgroundScheduler()


def start_controller():
    controller = Controller.build()
    controller.start_display()
    scheduler.add_job(controller.start_display, 'interval', seconds=5)
    scheduler.start()
    while True:
        controller.start_sensor(1)
        controller.start_sensor(2)


def run():
    thread = threading.Thread(target=start_controller)
    thread.daemon = True
    thread.start()
