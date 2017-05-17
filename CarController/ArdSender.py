import time

# Remplacer 0 par 1 si nouveau Raspberry
import smbus
class ArdSender(object):

    address = 0x12
    bus = smbus.SMBus(1)

    def __init__(self):
        self.bus = 0

    @staticmethod
    def sendCommand(code, description):
        ArdSender.bus.write_byte(ArdSender.address, code)
        print description, ArdSender.bus.read_byte(ArdSender.address)
