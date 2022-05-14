import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

class RelayController:
  def __init__(self, gpio):
    self.gpio = gpio

  @staticmethod
  def build(gpio_ids):
    [ GPIO.setup(gpio_id, GPIO.OUT) for gpio_id in gpio_ids ]
    return RelayController(GPIO)

  def on(self, gpio_id):
    self.gpio.output(gpio_id, self.gpio.LOW)

  def off(self, gpio_id):
    self.gpio.output(gpio_id, self.gpio.HIGH)

  def cleanup(self):
    GPIO.cleanup()
