from .controller import Controller
from time import sleep
import multiprocessing
import signal
from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)
scheduler = BackgroundScheduler()

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
  scheduler.add_job(controller.start_display, 'interval', seconds=4)
  scheduler.start()
  while not killer.kill_now:
    controller.start_sensor()
  server.terminate()
  server.join()
  controller.stop()
  scheduler.shutdown()

