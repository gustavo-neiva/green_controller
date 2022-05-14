import sys
from .app import GreenController
import signal

def main(args=None):
    if args is None:
        args = sys.argv[1:]
    controller = GreenController()
    signal.signal(signal.SIGINT, controller.stop)
    signal.signal(signal.SIGTERM, controller.stop)
    controller.run()

if __name__ == "__main__":
    sys.exit(main())