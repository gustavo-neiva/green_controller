from datetime import datetime
from green_controller.dht22_sensor import read
from green_controller.dht22_sensor import read
from green_controller.lcd import Lcd

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
        temp = f'Temp.={temperature:0.2f}*C'
        umidade = f'Umidade={humidity:0.2f}%'
        display.lcd_display_string(temp, 1)  # Write line of text to first line of display
        display.lcd_display_string(umidade, 2) 
        counter += 1
        if counter >= 130:
          humidity_medium = sum(humidities) / len(humidities)
          temp_medium = sum(temperatures) / len(temperatures)
          temp_medium_string = f'Temp.={temp_medium:0.2f}*C'
          humidity_medium_string = f'Umidade={humidity_medium:0.2f}%'
          print('****** MEDIA ******')
          print(f'{temp_medium_string} {humidity_medium_string}')
          display.lcd_clear()                                
          temperatures = []
          humidities = []
          counter = 0
  except KeyboardInterrupt:
      print("Limpando!")
      display.lcd_clear()