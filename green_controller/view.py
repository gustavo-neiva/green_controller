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
            self._print(temp, umidade)
            self.flag = False
            return
        ip = f'IP={ip}'
        hour = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self._print(ip, hour)
        self.flag = True

    def turn_off(self):
        self.display.clear()
        self._print("Limpando!", "Vlw flw!")
        self.display.clear()

    def _print(self, line1, line2):
        self.display.clear()
        self.display.print(line1, 1)
        self.display.print(line2, 2)
