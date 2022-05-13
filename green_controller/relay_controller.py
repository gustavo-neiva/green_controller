import RPi.GPIO as GPIO
 # GPIO Numbers instead of board numbers
RELAIS_1_GPIO = 12

class RelayController:

  def __init__(self, gpio):
    self.gpio = gpio

  @staticmethod
  def build(gpio_ids = [RELAIS_1_GPIO]):
    GPIO.setmode(GPIO.BCM)
    [ GPIO.setup(gpio_id, GPIO.OUT) for gpio_id in gpio_ids ]
    return RelayController(GPIO)

  def on(self, gpio_id = RELAIS_1_GPIO):
    self.gpio.output(gpio_id, self.gpio.LOW)

  def off(self, gpio_id = RELAIS_1_GPIO):
    self.gpio.output(gpio_id, self.gpio.HIGH)

  def cleanup(self):
    self.gpio.cleanup()