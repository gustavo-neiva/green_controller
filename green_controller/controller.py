from re import S
from subprocess import Popen, PIPE
from threading import Thread
import asyncio
from green_controller.sensor_controller import SensorController
from green_controller.view import View
from green_controller.relay_controller import RelayController
from green_controller.repository import Repository

LUZ_1 = 12
VENT_1 = 13
LUZ_2 = 6
VENT_2 = 5
relay_gpio_ids = [LUZ_1, VENT_1, LUZ_2, VENT_2]
DHT_SENSOR_1_PIN = 4
DHT_SENSOR_2_PIN = 14
sensors = {1: DHT_SENSOR_1_PIN, 2: DHT_SENSOR_2_PIN}


class Controller:
    @staticmethod
    def build():
        relay_controller = RelayController.build(relay_gpio_ids)
        view = View.build()
        sensor_controller = SensorController()
        repository = Repository()
        return Controller(relay_controller, view, sensor_controller, repository)

    def __init__(self, relay_controller, view, sensor_controller, repository):
        self.relay = relay_controller
        self.view = view
        self.sensor = sensor_controller
        self.repository = repository
        self.temperatures = []
        self.humidities = []
        self.counter = 0
        self.ip = self.parse_ip()
        self.first_sensor = True
        self.info_display = False

    def start_display(self):
        if self.first_sensor and not self.info_display:
            humidity, temperature, sensor_id = self.repository.get_last_measurement(
                1)
            self.view.display_sensor_data(temperature, humidity, sensor_id)
            self.first_sensor = False
        elif not self.first_sensor and not self.info_display:
            humidity, temperature, sensor_id = self.repository.get_last_measurement(
                2)
            self.view.display_sensor_data(temperature, humidity, sensor_id)
            self.info_display = True
        else:
            self.view.display_controller_info(self.ip)
            self.first_sensor = True
            self.info_display = False

    def start_sensor(self, id):
        humidity, temperature = asyncio.run(
            self.sensor.read(sensors[id]))
        print(humidity, temperature)
        self.repository.save_measurement(humidity, temperature, id)

    def stop(self):
        self.view.turn_off()
        self.relay.cleanup()

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

    def find_interface(self):
        find_device = "ip addr show"
        interface_parse = self.run_cmd(find_device)
        for line in interface_parse.splitlines():
            if "state UP" in line:
                dev_name = line.split(':')[1]
        return dev_name

    def run_cmd(self, cmd):
        p = Popen(cmd, shell=True, stdout=PIPE)
        output = p.communicate()[0]
        return output.decode('ascii')
