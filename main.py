from tlc1543 import ADC_Read, tlc1543_int, abs_my
import time
from DustSensor import DustSensor
from DHTSensor import DHTSensor
import requests
import mh_z19
from numpy import random
import numpy as np
import smbus2
from sgp30 import SGP30
# import Rpi.GPIO as GPIO
# import gpiod

CHANNEL = 6
dust_sensor = DustSensor(channel=CHANNEL)
dht_sensor = DHTSensor()

device_access_token = "iqrdw650qvas7poccfla"
url = f"https://upc.famnkunf.xyz/api/v1/{device_access_token}/telemetry"

# curl -v -X POST https://upc.famnkunf.xyz/api/v1/iqrdw650qvas7poccfla/telemetry --header Content-Type:application/json --data "{temperature:25}"

print("Starting")
sgp30 = SGP30()
sgp30.start_measurement()
#co2_l = [500] * 10
try:
    while True:
        payload = {}
        try:
            dust_density = dust_sensor.read_converted_value()
            payload['dust_density'] = round(dust_density,4)
            print("Current dust concentration: %.4f ug/m3" % dust_density)
        except:
            print("Error with dust sensor")
            pass
        try:
            temperature, humidity = dht_sensor.get_value()
            payload['temperature'] = round(temperature,4) 
            payload['humidity'] = round(humidity, 4)
            print("Temperature: {:.4f} C, Humidity: {:.4%}".format(temperature, humidity/100))
        except:
            print("Error with DHT")
            pass
        try:
            results = sgp30.get_air_quality()
            eco2 = results.equivalent_co2
            tvoc = results.total_voc
            print("eCO2: {:.4f}, TVOC: {:.4f}".format(eco2, tvoc))
            #co2 = mh_z19.read()['co2']
            #print("Co2 level:", co2)
            #payload['co2'] = co2
            payload['eco2'] = eco2
            payload['tvoc'] = tvoc
        except Exception as e:
            print(e)
            print("Error with SGP30 sensor")
            #co2 = 500 + random.normal(loc=0, scale=20)
            #co2_l.append(co2)
            #co2_l.pop(0)
            #co2 = np.mean(co2_l)
            #payload['co2'] = round(co2, 4)
            #print("There is some error acquiring CO2")
            #print("Setting random co2 value:", co2)
        requests.post(url, json=payload, headers={"Content-Type": "application/json"})
        time.sleep(1)
except Exception as e:
    print(e)
