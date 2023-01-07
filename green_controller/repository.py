from green_controller.model import *


class Repository:

    def save_measurement(self, humidity, temperature, sensor_id):
        data = Measurements.create(
            humidity=humidity, temperature=temperature, sensor_id=sensor_id)
        data.save()

    def get_last_measurement(self):
        last_measurement = Measurements.select().order_by(Measurements.id.desc()).get()
        humidity = last_measurement.humidity
        temperature = last_measurement.temperature
        sensor_id = last_measurement.sensor_id
        return humidity, temperature, sensor_id
