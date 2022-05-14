from .controller import Controller
from time import sleep
import signal

class GracefulKiller:
  kill_now = False
  def __init__(self):
    signal.signal(signal.SIGINT, self.exit_gracefully)
    signal.signal(signal.SIGTERM, self.exit_gracefully)

  def exit_gracefully(self, *args):
    self.kill_now = True

def run():
    controller = Controller.build()
    killer = GracefulKiller()
    while not killer.kill_now:
        controller.start()
    controller.stop()