#!/usr/bin/python
# -*- coding:utf-8 -*-
# import RPi.GPIO as GPIO
from gpiozero import LED, Button
import time
#import math

#import sys

# Clock = 16
Clock = LED(16)
# Address = 20
Address = LED(20)
# DataOut = 21
DataOut = Button(21)

CHANNEL = 6 # selector channel

flag_error = 0

def abs_my(x,y):
    i = 0
    if( x >> y ):
        i = x - y
    elif( x <= y ):
        i = y - x
    return i

def tlc1543_int():
    for i in range(0,flag_error):
# 		GPIO.output(Clock ,GPIO.HIGH)
#		time.sleep(0.00001)
# 		GPIO.output(Clock ,GPIO.LOW)
#		time.sleep(0.00001)
        Clock.on()
        Clock.off()
def ADC_Read(channel):
    value = 0;
    for i in range(0,4):
        if((channel >> (3 - i)) & 0x01):
#                         GPIO.output(Address,GPIO.HIGH)
            Address.on()
        else:
#                         GPIO.output(Address,GPIO.LOW)
            Address.off()
#                 GPIO.output(Clock,GPIO.HIGH)
#               time.sleep(0.00001)
#                 GPIO.output(Clock,GPIO.LOW)
#                time.sleep(0.00001)
        Clock.on()
        Clock.off()
    for i in range(0,6):
#                 GPIO.output(Clock,GPIO.HIGH)
#                time.sleep(0.00001)
#                 GPIO.output(Clock,GPIO.LOW)
#                time.sleep(0.00001)
        Clock.on()
        Clock.off()
    time.sleep(0.001)
    for i in range(0,10):
#                 GPIO.output(Clock,GPIO.HIGH)
        Clock.on()
#                time.sleep(0.00001)
        value <<= 1
        if(not DataOut.is_pressed):
            value |= 0x01
#                 GPIO.output(Clock,GPIO.LOW)
        Clock.off()
#                time.sleep(0.00001)
    return value

# GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)
# GPIO.setup(Clock,GPIO.OUT)
# GPIO.setup(Address,GPIO.OUT)
# GPIO.setup(DataOut,GPIO.IN,GPIO.PUD_UP)

# tmp = [0,0,0,0,0,0]
# k = [0,0,0,0,0,0]
# value = 0 
# try:
# 	while True:
# 		tlc1543_int()
# 		tmp[0] = ADC_Read(CHANNEL)
# 		time.sleep(0.001)
# 		tmp[1] = ADC_Read(CHANNEL)
# 		time.sleep(0.001)
# 		tmp[2] = ADC_Read(CHANNEL)
# 		time.sleep(0.001)
# 		tmp[3] = ADC_Read(CHANNEL)
# 		time.sleep(0.001)
# 		tmp[4] = ADC_Read(CHANNEL)
# 		time.sleep(0.001)
# 		tmp[5] = ADC_Read(CHANNEL)
# 		time.sleep(0.001)
# 		
# 		k[0] = abs_my(tmp[1],tmp[0])
# 		k[1] = abs_my(tmp[2],tmp[1])
# 		k[2] = abs_my(tmp[3],tmp[2])
# 		k[3] = abs_my(tmp[4],tmp[3])
# 		k[4] = abs_my(tmp[5],tmp[4])
# 		
# 		if ( (k[0] > 3) or (k[1] > 3) or (k[2] > 3) or (k[3] > 3) or (k[4] > 3) ):
# 			flag_error = flag_error + 1
# 			if (flag_error==21):
# 				flag_error = 0
# # 			print("Busy or Not give a Voltage at Pin T_A%d" %CHANNEL)
# 			time.sleep(0.001)
# 		elif ( (k[0] <= 3) and (k[1] <= 3) and (k[2] <= 3) and (k[3] <= 3) and (k[4] <= 3)  ):
# 			flag_error = 0
# 			value = (tmp[0] + tmp[1] + tmp[2] + tmp[3] + tmp[4] + tmp[5])/6
# 			print("AD: %d"%value)
# 			time.sleep(0.3)
# 		else:
# 			flag_error = 0
# 			print("err: %d"%ADC_Read(6))
# 			print("Busy or Not give a Voltage at Pin T_A6")
# # 			print("AD: %d"%ADC_Read(6))
# 			time.sleep(0.1)
# except:
#         GPIO.cleanup()

#sys.exit()
