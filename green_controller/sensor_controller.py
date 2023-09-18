import Adafruit_DHT
import asyncio

DHT_SENSOR = Adafruit_DHT.DHT22


class SensorController:
    def __init__(self, sensor=DHT_SENSOR):
        self.sensor = sensor

    async def read(self, pin):
        humidity, temperature = Adafruit_DHT.read_retry(self.sensor, pin)
        print(humidity, temperature)
        if humidity is not None and temperature is not None:
            await asyncio.sleep(1)
            return humidity, temperature
