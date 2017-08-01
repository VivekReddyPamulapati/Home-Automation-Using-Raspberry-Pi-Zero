#Home Automation Using Raspberry Pi
#Intruder Detection System
#Camera Section
#Save this file as Intruder.py
#Create a folder named /var/www/html/Intruder_Images

import RPi.GPIO as GPIO
import time, datetime
import pygame, sys
from pygame.locals import *
import pygame.camera

dateString = '%Y-%m-%d %H-%M-%S'
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
	z= datetime.datetime.now().strftime(dateString)#STORING DATE AND TIME IN A VARIABLE
	print z #PRINTING THE DATE AND TIME OF INTRUSION
	pygame.init() #CAMERA SECTION
        pygame.camera.init()
        cam = pygame.camera.Camera("/dev/video0",(1280,720))
        cam.start()
        image= cam.get_image()
        pygame.image.save(image,'/var/www/html/Intruder_Images/%s.jpg'%str(z))
        cam.stop()
	GPIO.output(buz,GPIO.LOW)
