from .controller import Controller
from time import sleep
import threading
import signal
import logging
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()
event = threading.Event()


class GracefulKiller:
    kill_now = False

    def __init__(self, scheduler, controller):
        self.scheduler = scheduler
        self.controller = controller
        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)

    def exit_gracefully(self, *args):
        print('terminando o programa ********* shutting down')
        self.kill_now = True
        self.scheduler.shutdown()
        print('scheduler finalizado')
        self.controller.stop()
        print('finalizadoooooo')


def run():
    controller = Controller.build()
    killer = GracefulKiller(scheduler, controller)
    controller.start_display()
    scheduler.add_job(controller.start_display, 'interval', seconds=5)
    scheduler.start()
    while not killer.kill_now:
        controller.start_sensor(1)
        controller.start_sensor(2)
