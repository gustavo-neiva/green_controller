from datetime import datetime
from time import sleep
from green_controller.dht22_sensor import read
from green_controller.dht22_sensor import read
from green_controller.lcd import Lcd
from green_controller.relay_controller import RelayController

RELAIS_1_GPIO = 12
RELAIS_2_GPIO = 13
RELAIS_3_GPIO = 6
RELAIS_4_GPIO = 5
gpio_ids = [RELAIS_1_GPIO, RELAIS_2_GPIO, RELAIS_3_GPIO, RELAIS_4_GPIO]
relay = RelayController.build(gpio_ids)
display = Lcd()
active = True

def run():
  counter = 0
  start_time = datetime.now()
  print('Inicio: {}'.format(start_time))
  try:
    while active:
        temperatures = []
        humidities = []
        humidity, temperature = read()

        temperatures.append(temperature)
        humidities.append(humidity)
        
        if temperature >= 25:
          relay.on(RELAIS_1_GPIO)
          relay.on(RELAIS_2_GPIO)
          relay.off(RELAIS_3_GPIO)
          relay.off(RELAIS_4_GPIO)
        if temperature > 22 and temperature < 25:
          relay.off(RELAIS_1_GPIO)
          relay.off(RELAIS_2_GPIO)
          relay.on(RELAIS_3_GPIO)
          relay.on(RELAIS_4_GPIO)

        temp = f'Temp.={temperature:0.2f}*C'
        umidade = f'Umidade={humidity:0.2f}%'
        print(f'{temp} {umidade}')

        display.lcd_display_string(temp, 1)
        display.lcd_display_string(umidade, 2) 
        counter += 1

        if counter >= 130:
          humidity_medium = sum(humidities) / len(humidities)
          temp_medium = sum(temperatures) / len(temperatures)
          temp_medium_string = f'Temp.={temp_medium:0.2f}*C'
          humidity_medium_string = f'Umidade={humidity_medium:0.2f}%'
          print('****** MEDIA ******')
          print(f'{temp_medium_string} {humidity_medium_string}')
          temperatures = []
          humidities = []
          counter = 0
  except KeyboardInterrupt:
      relay.cleanup()
      sleep(1)
      print("Limpando!")
      display.lcd_clear()

def stop():
  active = False
  relay.cleanup()
  sleep(1)
  print("Limpando!")
  display.lcd_clear()
