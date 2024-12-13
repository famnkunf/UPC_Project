from tlc1543 import ADC_Read, tlc1543_int, abs_my
import numpy as np
# import RPi.GPIO as GPIO
from gpiozero import LED, Button
import time

class DustSensor:
    def __init__(self, channel=6, sys_voltage=3300, n=10):
        self.CHANNEL = channel
        self.SYS_VOLTAGE = sys_voltage
        self.buffer_len = n
        self.buffer = [0] * self.buffer_len
        self.flag_first = 0
        self.sum1 = 0
        self.NO_DUST_VOLTAGE = 600
#         self.NO_DUST_VOLTAGE = 200
        self.COV_RATIO = 0.2
#         self.DIN = 17
        self.DIN = LED(17)
#         GPIO.setmode(GPIO.BCM)
#         GPIO.setwarnings(False)
#         GPIO.setup(self.DIN, GPIO.OUT)
    def read_value(self):
        return ADC_Read(self.CHANNEL)
    def filtered_value(self):
        ad_value = self.read_value()
#         print(ad_value)
        if self.flag_first == 0:
            self.flag_first = 1
            for i in range (self.buffer_len):
                self.buffer[i] = ad_value
                self.sum1 = self.sum1+self.buffer[i]
            return ad_value
        else:
            self.sum1 = self.sum1-self.buffer[0]
            for i in range (self.buffer_len-1):
                self.buffer[i] = self.buffer[i+1]
            self.buffer[9] = ad_value
            self.sum1 = self.sum1 + self.buffer[9]
            i = self.sum1 / 10.0
            return i
    def read_converted_value(self):
#         GPIO.output(self.DIN, GPIO.HIGH)
        self.DIN.on()
        time.sleep(0.0028)
        voltage = (self.SYS_VOLTAGE / 1024) * self.filtered_value() * 11
        time.sleep(0.0004)
#         GPIO.output(self.DIN, GPIO.LOW)
        self.DIN.off()
        if voltage >= self.NO_DUST_VOLTAGE:
            voltage = voltage - self.NO_DUST_VOLTAGE
            density = voltage * self.COV_RATIO
        else:
            density = 0
        return density