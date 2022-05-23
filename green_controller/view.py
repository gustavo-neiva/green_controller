from time import sleep
from datetime import datetime
from green_controller.display_controller import DisplayController

class View:
  @staticmethod
  def build():
    display = DisplayController.build()
    return View(display)

  def __init__(self, display):
    self.display = display
    self.flag = True

  def display_data(self, temperature, humidity, ip):
    if self.flag:
      temp = f'Temp.={temperature:0.2f}*C'
      umidade = f'Umidade={humidity:0.2f}%'
      print(temp)
      print(umidade)
      self.display.clear()
      self.display.print(temp, 1)
      self.display.print(umidade, 2)
      self.flag = False
    else:
      hour = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
      ip = f'IP={ip}'
      print(hour)
      print(ip)
      self.display.clear()
      self.display.print(ip, 1)
      self.display.print(hour, 2)
      self.flag = True
    
  def turn_off(self):
    sleep(5)
    self.display.clear()
    self.display.print("Limpando!", 1)
    self.display.print("Vlw flw!", 2)
    sleep(5)
    self.display.clear()
