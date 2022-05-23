from .controller import Controller
from time import sleep
import multiprocessing
from threading import Thread
import signal
from flask import Flask

app = Flask(__name__)

class GracefulKiller:
  kill_now = False
  def __init__(self):
    signal.signal(signal.SIGINT, self.exit_gracefully)
    signal.signal(signal.SIGTERM, self.exit_gracefully)

  def exit_gracefully(self, *args):
    self.kill_now = True

@app.route('/')
def index():
  return 'Hello world'

def run_flask():
  app.run(debug=True, host='0.0.0.0')

def run():
  controller = Controller.build()
  killer = GracefulKiller()
  server = multiprocessing.Process(target=run_flask)
  server.start()
  while not killer.kill_now:
    controller.start()
  server.terminate()
  server.join()
  controller.stop()

