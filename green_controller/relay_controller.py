import RPi.GPIO as GPIO
 # GPIO Numbers instead of board numbers
RELAIS_1_GPIO = 12

class RelayController:
  def build(self, gpio_ids = [RELAIS_1_GPIO]):
    GPIO.setmode(GPIO.BCM)
    [ GPIO.setup(gpio_id, GPIO.OUT) for gpio_id in gpio_ids ]

  def on(self, gpio_id = RELAIS_1_GPIO):
    GPIO.output(gpio_id, GPIO.LOW)

  def off(self, gpio_id = RELAIS_1_GPIO):
    GPIO.output(gpio_id, GPIO.HIGH)

  def cleanup(self):
    GPIO.cleanup()