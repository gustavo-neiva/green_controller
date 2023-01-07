from green_controller.model import *


class Repository:

    def save_measurement(self, humidity, temperature):
        data = Measurements.create(humidity=humidity, temperature=temperature)
        data.save()

    def get_last_measurement(self):
        last_measurement = Measurements.select().order_by(Measurements.id.desc()).get()
        humidity = last_measurement.humidity
        temperature = last_measurement.temperature
        return humidity, temperature
