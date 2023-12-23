import serial
from serial.tools import list_ports


class ArduinoController:
    def __init__(self, baud_rate=9600):
        self.port = self.find_arduino_port()
        if self.port:
            self.ser = serial.Serial(self.port, baud_rate, timeout=1)
        else:
            raise RuntimeError(
                "Arduino not found. Please make sure it is connected.")

    def find_arduino_port(self):
        arduino_ports = [
            p.device
            for p in list_ports.comports()
            if 'Arduino' in p.description or 'USB Serial Device' in p.description
        ]
        if arduino_ports:
            return arduino_ports[0]
        else:
            return None

    def turn_on(self):
        self.ser.write(b'1')

    def turn_off(self):
        self.ser.write(b'0')
