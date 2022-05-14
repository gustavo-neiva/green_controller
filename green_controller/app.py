from .controller import Controller
import signal

class GracefulKiller:
  kill_now = False
  def __init__(self, controller):
    self.controller = controller
    signal.signal(signal.SIGINT, self.exit_gracefully)
    signal.signal(signal.SIGTERM, self.exit_gracefully)

  def exit_gracefully(self, *args):
    self.controller.stop()
    self.kill_now = True

def run():
    controller = Controller.build()
    killer = GracefulKiller(controller)
    while not killer.kill_now:
        controller.start()