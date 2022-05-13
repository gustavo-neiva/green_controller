from datetime import datetime
from green_controller.dht22_sensor import read
from green_controller.dht22_sensor import read
from green_controller.lcd import Lcd
from green_controller.relay_controller import RelayController

relay = RelayController.build()

def run():
  display = Lcd()
  counter = 0
  start_time = datetime.now()
  print('Inicio: {}'.format(start_time))
  try:
    while True:
        temperatures = []
        humidities = []
        humidity, temperature = read()

        temperatures.append(temperature)
        humidities.append(humidity)
        
        if temperature <= 25:
          relay.on()
        else:
          relay.off()

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
      display.lcd_clear()
      print("Limpando!")