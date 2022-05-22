from green_controller.model import *

class Repository:
  
  def save_measurement(self, humidity, temperature):
    data = Measurements.create(humidity=humidity, temperature=temperature)
    data.save()

  def get_last_measurement(self, humidity, temperature):
    data = Measurements.create(humidity=humidity, temperature=temperature)
    data.save()

