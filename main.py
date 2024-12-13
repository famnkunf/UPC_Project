from tlc1543 import ADC_Read, tlc1543_int, abs_my
import time
from DustSensor import DustSensor
from DHTSensor import DHTSensor
import request
# import Rpi.GPIO as GPIO
# import gpiod

CHANNEL = 6
dust_sensor = DustSensor(channel=CHANNEL)
dht_sensor = DHTSensor()

print("Starting")
try:
    while True:
        value = dust_sensor.read_converted_value()
        temperature, humidity = dht_sensor.get_value()
        print("Current dust concentration: %.4f ug/m3" % value)
        print("Temperature: {:.4f} C, Humidity: {:.4%}".format(temperature, humidity/100))
        time.sleep(0.1)
except Exception as e:
    print(e)
