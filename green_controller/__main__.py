from .app import GreenController
import signal

controller = GreenController.build()

class GracefulKiller:
  kill_now = False
  def __init__(self):
    signal.signal(signal.SIGINT, self.exit_gracefully)
    signal.signal(signal.SIGTERM, self.exit_gracefully)

  def exit_gracefully(self, *args):
    controller.stop()
    self.kill_now = True
   

if __name__ == '__main__':
    killer = GracefulKiller()
    while not killer.kill_now:
        controller.run()