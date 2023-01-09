import threading

from .app import run
from .server import run_flask


def start_controller():
    t = threading.Thread(target=run)
    t.daemon = True
    t.start()


if __name__ == '__main__':
    start_controller()
    run_flask()
