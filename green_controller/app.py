from .controller import Controller
from time import sleep
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
async def index():
    controller = Controller.build()
    killer = GracefulKiller()
    while not killer.kill_now:
      await controller.start()
    controller.stop()

async def run():
    await app.run(debug=True, host='0.0.0.0')
