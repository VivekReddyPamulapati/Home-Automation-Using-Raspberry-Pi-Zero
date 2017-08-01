#Makerdemy
#Home Automation Using Raspberry Pi
#Intruder Detection System
#Motion Detection Section
#Save the file as Intruder.py

import RPi.GPIO as GPIO
import time, datetime

pir=8
buz=10
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pir,GPIO.IN)
GPIO.setup(buz,GPIO.OUT)

GPIO.output(buz,GPIO.LOW)
time.sleep(5) #SETTING UP THE SENSOR
print("SENSOR is READY")

while True:
    x=GPIO.input(pir)
    if x==1:
	GPIO.output(buz,GPIO.HIGH)
	print("ALERT!!!INTRUSION DETECTED at PIR1")
	GPIO.output(buz,GPIO.LOW)
