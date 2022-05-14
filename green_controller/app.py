from datetime import datetime
from time import sleep
from green_controller.dht22_sensor import read
from green_controller.lcd import Lcd
from green_controller.relay_controller import RelayController

RELAIS_1_GPIO = 12
RELAIS_2_GPIO = 13
RELAIS_3_GPIO = 6
RELAIS_4_GPIO = 5
gpio_ids = [RELAIS_1_GPIO, RELAIS_2_GPIO, RELAIS_3_GPIO, RELAIS_4_GPIO]
relay = RelayController.build(gpio_ids)

class GreenController:
  def __init__(self):
    self.relay = relay
    self.display = Lcd()
    self.temperatures = []
    self.humidities = []
    self.counter = 0

  def run(self):
    humidity, temperature = read()
    if humidity is not None and temperature is not None:
      self.temperatures.append(temperature)
      self.humidities.append(humidity)
      
      if temperature >= 25:
        self.relay.on(RELAIS_1_GPIO)
        self.relay.on(RELAIS_2_GPIO)
        self.relay.off(RELAIS_3_GPIO)
        self.relay.off(RELAIS_4_GPIO)
      if temperature > 22 and temperature < 25:
        self.relay.off(RELAIS_1_GPIO)
        self.relay.off(RELAIS_2_GPIO)
        self.relay.on(RELAIS_3_GPIO)
        self.relay.on(RELAIS_4_GPIO)

      temp = f'Temp.={temperature:0.2f}*C'
      umidade = f'Umidade={humidity:0.2f}%'
      print(f'{temp} {umidade}')

      self.display.lcd_display_string(temp, 1)
      self.display.lcd_display_string(umidade, 2) 
      self.counter += 1

      if self.counter >= 130:
        humidity_medium = sum(humidities) / len(humidities)
        temp_medium = sum(temperatures) / len(temperatures)
        temp_medium_string = f'Temp.={temp_medium:0.2f}*C'
        humidity_medium_string = f'Umidade={humidity_medium:0.2f}%'
        print('****** MEDIA ******')
        print(f'{temp_medium_string} {humidity_medium_string}')
        temperatures = []
        humidities = []
        self.counter = 0

  def stop(self):
    sleep(1)
    print("Limpando!")
    self.display.lcd_clear()
    self.relay.cleanup()
