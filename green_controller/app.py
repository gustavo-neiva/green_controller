from .controller import Controller
from time import sleep
import signal
import asyncio
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'

class GracefulKiller:
  kill_now = False
  def __init__(self):
    signal.signal(signal.SIGINT, self.exit_gracefully)
    signal.signal(signal.SIGTERM, self.exit_gracefully)

  def exit_gracefully(self, *args):
    self.kill_now = True

async def run():
    app.run(debug=True, host='0.0.0.0')
    controller = Controller.build()
    killer = GracefulKiller()
    while not killer.kill_now:
      await controller.start()
    controller.stop()