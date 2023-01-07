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

    def display_sensor_data(self, temperature, humidity, sensor_id):
        temp = f'{temperature:0.2f}*C id={sensor_id}'
        umidade = f'Umidade={humidity:0.2f}%'
        self._print(temp, umidade)

    def display_controller_info(self, ip):
        ip = f'IP={ip}'
        hour = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self._print(ip, hour)

    def turn_off(self):
        self.display.clear()
        self._print("Limpando!", "Vlw flw!")
        self.display.clear()

    def _print(self, line1, line2):
        self.display.clear()
        self.display.print(line1, 1)
        self.display.print(line2, 2)
