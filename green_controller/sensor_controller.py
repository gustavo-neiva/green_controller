import Adafruit_DHT
import asyncio

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4


class SensorController:
    def __init__(self, sensor=DHT_SENSOR, pin=DHT_PIN):
        self.sensor = sensor
        self.pin = pin

    async def read(self):
        humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.pin)
        if humidity is not None and temperature is not None:
            await asyncio.sleep(1)
            return humidity, temperature
