from time import sleep
from datetime import datetime
import asyncio
from green_controller.display_controller import DisplayController

class View:
  @staticmethod
  def build():
    display = DisplayController.build()
    return View(display)

  def __init__(self, display):
    self.display = display

  async def display_data(self, temperature, humidity, ip):
      hour = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
      temp = f'Temp.={temperature:0.2f}*C'
      umidade = f'Umidade={humidity:0.2f}%'
      ip = f'IP={ip}'
      print('indo printar temp')
      await asyncio.sleep(3)
      self.display.clear()
      self.display.print(temp, 1)
      self.display.print(umidade, 2)
      print('pritou temp')
      await asyncio.sleep(3)
      print('agora é ip')
      self.display.clear()
      self.display.print(ip, 1)
      self.display.print(hour, 2)
      print('foi')
    
  def turn_off(self):
    self.display.clear()
    self.display.print("Limpando!", 1)
    self.display.print("Vlw flw!", 2)
    sleep(2)
    self.display.clear()
