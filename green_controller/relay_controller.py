import RPi.GPIO as GPIO


class RelayController:
    @staticmethod
    def build(gpio_ids):
        GPIO.setmode(GPIO.BCM)
        [GPIO.setup(gpio_id, GPIO.OUT) for gpio_id in gpio_ids]
        return RelayController()

    def on(self, gpio_id):
        GPIO.output(gpio_id, GPIO.LOW)

    def off(self, gpio_id):
        GPIO.output(gpio_id, GPIO.HIGH)

    def cleanup(self):
        GPIO.cleanup()
