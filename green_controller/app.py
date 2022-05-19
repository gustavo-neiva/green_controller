from .controller import Controller
from time import sleep
import threading
import signal
import asyncio
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

async def run_sensors():
  controller = Controller.build()
  killer = GracefulKiller()
  while not killer.kill_now:
    await controller.start()
  controller.stop()

async def run():
  thread = threading.Thread(target=run_sensors)
  await thread.start()
  app.run(debug=True, host='0.0.0.0')
