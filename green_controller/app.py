from datetime import datetime
from green_controller.dht22_sensor import read
from green_controller.dht22_sensor import read
from green_controller.lcd import Lcd

def run():
  display = Lcd()
  counter = 0
  start_time = datetime.now()
  print('Inicio: {}'.format(start_time))
  while True:
      temperatures = []
      humidities = []
      humidity, temperature = read()
      temperatures.append(temperature)
      humidities.append(humidity)
      temp = f'Temperatura={temperature:0.2f}*C'
      umidade = f'Umidade={humidity:0.2f}%"'
      display.lcd_display_string(temp, 1)  # Write line of text to first line of display
      display.lcd_display_string(umidade, 2) 
      counter += 1
      if counter >= 130:
        humidity_medium = sum(humidities) / len(humidities)
        temp_medium = sum(temperatures) / len(temperatures)
        temp_medium_string = f'Temperatura={temp_medium:0.2f}*C'
        humidity_medium_string = f'Umidade={humidity_medium:0.2f}%"'
        print('****** MEDIA ******')
        display.lcd_display_string('****** MEDIA ******', 1)  # Write line of text to first line of display
        display.lcd_display_string('****** MEDIA ******', 2) 
        display.lcd_display_string(temp_medium_string, 1)  # Write line of text to first line of display
        display.lcd_display_string(humidity_medium_string, 2) 
        print(f'{temp_medium_string} {humidity_medium_string}')
        display.lcd_clear()                                
        temperatures = []
        humidities = []
        counter = 0