from subprocess import Popen, PIPE
from datetime import datetime
from time import sleep
from green_controller.sensor_controller import SensorController
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
    display_controller = DisplayController.build()
    sensor_controller = SensorController()
    return Controller(relay_controller, display_controller, sensor_controller)

  def __init__(self, relay_controller, display_controller, sensor_controller):
    self.relay = relay_controller
    self.display = display_controller
    self.sensor = sensor_controller
    self.temperatures = []
    self.humidities = []
    self.counter = 0

  def start(self):
    humidity, temperature = self.sensor.read()
    if humidity is not None and temperature is not None:
      temp = f'Temp.={temperature:0.2f}*C'
      umidade = f'Umidade={humidity:0.2f}%'

      print(self.find_interface())

      self.display.print(temp, 1)
      self.display.print(umidade, 2)

  def stop(self):
    self.display.clear()
    self.display.print("Limpando!", 1)
    self.display.print("Vlw flw!", 2)
    sleep(2)
    self.relay.cleanup()
    self.display.clear()

  def find_interface(self):
    find_device = "ip addr show"
    interface_parse = self.run_cmd(find_device)
    for line in interface_parse.splitlines():
        if "state UP" in line:
            dev_name = line.split(':')[1]
    return dev_name

  def parse_ip(self):
    interface = self.find_interface()
    find_ip = "ip addr show %s" % interface
    find_ip = "ip addr show %s" % interface
    ip_parse = self.run_cmd(find_ip)
    for line in ip_parse.splitlines():
        if "inet " in line:
            ip = line.split(' ')[5]
            ip = ip.split('/')[0]
    return ip

  def run_cmd(self, cmd):
    p = Popen(cmd, shell=True, stdout=PIPE)
    output = p.communicate()[0]
    return output.decode('ascii')
