import threading

from .app import run
from .server import run_flask


def start_controller():
    thread = threading.Thread(target=run)
    thread.daemon = True
    thread.start()


if __name__ == '__main__':
    start_controller()
    run_flask()
