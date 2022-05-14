from .app import GreenController
import signal

controller = GreenController()

class GracefulKiller:
  kill_now = False
  def __init__(self):
    signal.signal(signal.SIGINT, self.exit_gracefully)
    signal.signal(signal.SIGTERM, self.exit_gracefully)

  def exit_gracefully(self, *args):
    controller.stop()
    self.kill_now = True
   
  print("End of the program. I was killed gracefully :)")

def main(args=None):
    controller.run()

if __name__ == '__main__':
    killer = GracefulKiller()
    while not killer.kill_now:
        main()