import Adafruit_DHT
from datetime import datetime

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

def read_data():
  counter = 0
  start_time = datetime.now()
  print('Inicio: {}'.format(start_time))
  while True:
      temperatures = []
      humidities = []
      humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
      temperatures.append(temperature)
      humidities.append(humidity)
      print("Temperatura={0:0.1f}*C  Umidade={1:0.1f}%".format(temperature, humidity))
      counter += 1
      if counter >= 130:
        humidity_medium = sum(humidities) / len(humidities)
        temp_medium = sum(temperatures) / len(temperatures)
        print('****** MEDIA ******')
        print("Temperatura={0:0.1f}*C  Umidade={1:0.1f}%".format(temp_medium, humidity_medium))
        temperatures = []
        humidities = []
        counter = 0
