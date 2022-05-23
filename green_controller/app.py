from .controller import Controller
from time import sleep
import threading
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
  print('flask foi')
  app.run(debug=True, host='0.0.0.0', suse_reloader=False)

def run():
  controller = Controller.build()
  killer = GracefulKiller()
  scheduler.add_job(controller.start_display, 'interval', seconds=3)
  print('iniciou jobs')
  scheduler.start()
  server = threading.Thread(target=run_flask)
  server.start()
  while not killer.kill_now:
    controller.start_sensor()
  server.join()
  controller.stop()
  scheduler.shutdown()

