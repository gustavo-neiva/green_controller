from green_controller.lcd import Lcd


class DisplayController:
  @staticmethod
  def build():
    lcd = Lcd()
    return DisplayController(lcd)

  def __init__(self, lcd):
    self.lcd = lcd

  def print(self, string, line):
    self.lcd.lcd_display_string(string, line)

  def clear(self):
    self.lcd.lcd_clear()