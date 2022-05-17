import Adafruit_DHT

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4


class SensorController:
  def __init__(self, sensor = DHT_SENSOR, pin = DHT_PIN):
    self.sensor = sensor
    self.pin = pin

  def read(self):
    humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.pin)
    if humidity is not None and temperature is not None:
      return humidity, temperature