from time import sleep
from green_controller.dht22_sensor import read
from green_controller.display_controller import DisplayController
from green_controller.relay_controller import RelayController

LUZ_1 = 12
VENT_1 = 13
LUZ_2 = 6
VENT_2 = 5
relay_gpio_ids = [LUZ_1, VENT_1, LUZ_2, VENT_2]

class Controller:
  @staticmethod
  def build():
    relay_controller = RelayController.build(relay_gpio_ids)
    display_controller = DisplayController()
    return Controller(relay_controller, display_controller)

  def __init__(self, relay_controller, display_controller):
    self.relay = relay_controller
    self.display = display_controller
    self.temperatures = []
    self.humidities = []
    self.counter = 0

  def start(self):
    humidity, temperature = read()
    if humidity is not None and temperature is not None:
      self.temperatures.append(temperature)
      self.humidities.append(humidity)
      
      if temperature >= 25:
        self.relay.on(VENT_1)
        self.relay.on(VENT_2)
      if temperature > 22 and temperature < 25:
        self.relay.off(VENT_1)
        self.relay.off(VENT_2)

      temp = f'Temp.={temperature:0.2f}*C'
      umidade = f'Umidade={humidity:0.2f}%'
      print(f'{temp} {umidade}')

      self.display.print(temp, 1)
      self.display.print(umidade, 2) 
      self.counter += 1

      if self.counter >= 130:
        humidity_medium = sum(self.humidities) / len(self.humidities)
        temp_medium = sum(self.temperatures) / len(self.temperatures)
        temp_medium_string = f'Temp.={temp_medium:0.2f}*C'
        humidity_medium_string = f'Umidade={humidity_medium:0.2f}%'
        print(f'{temp_medium_string} {humidity_medium_string}')
        self.temperatures = []
        self.humidities = []
        self.counter = 0

  def stop(self):
    print("Limpando!")
    self.display.clear()
    self.display.print("Limpando!", 1)
    self.display.print("Vlw flw!", 2)
    sleep(1)
    self.display.clear()
    self.relay.cleanup()
    return 