from time import sleep
import multiprocessing
import asyncio
from green_controller.display_controller import DisplayController

class View:
  @staticmethod
  def build():
    display = DisplayController.build()
    return View(display)

  def __init__(self, display):
    self.display = display

  async def display_data(self, temperature, humidity, ip, hour):
      temp = f'Temp.={temperature:0.2f}*C'
      umidade = f'Umidade={humidity:0.2f}%'
      ip = f'IP={ip}'
      self.display.clear()
      self.display.print(temp, 1)
      self.display.print(umidade, 2)
      await asyncio.sleep(3)
      self.display.clear()
      self.display.print(ip, 1)
      self.display.print(hour, 2)
      await asyncio.sleep(3)
    
  def turn_off(self):
    self.process.terminate()
    self.display.clear()
    self.display.print("Limpando!", 1)
    self.display.print("Vlw flw!", 2)
    sleep(2)
    self.display.clear()
