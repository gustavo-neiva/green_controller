import RPi.GPIO as GPIO

class RelayController:
  @staticmethod
  def build(gpio_ids):
    GPIO.setmode(GPIO.BCM)
    [ GPIO.setup(gpio_id, GPIO.OUT) for gpio_id in gpio_ids ]
    return RelayController()

  def on(self, gpio_id):
    try:
      GPIO.output(gpio_id, GPIO.LOW)
    except RuntimeError as e:
      print('errou on', e)

  def off(self, gpio_id):
    try:
      GPIO.output(gpio_id, GPIO.HIGH)
    except RuntimeError as e:
      print('errou off', e)

  def cleanup(self):
    try:
      GPIO.cleanup()
    except RuntimeError as e:
      print('errou cleanup', e)