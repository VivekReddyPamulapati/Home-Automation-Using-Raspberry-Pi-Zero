#Home Automation Using Raspberry Pi
#Intruder Detection System
#Save this file at /var/www/html/Intruder.py
#Create a folder named /var/www/html/Intruder_Images
#Create a database named 'intruder' with table PIR1 and fields, DateTime and Image
#Type your From and To address and Password appropriately

import RPi.GPIO as GPIO
import time, datetime
import smtplib
import pygame, sys
from pygame.locals import *
import pygame.camera
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
import MySQLdb

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
	path='/var/www/html/Intruder_Images/'+str(z)+'.jpg' #DATABASE SECTION
        db=MySQLdb.connect("localhost","root","12345678","intruder")
        curs=db.cursor()
        with db:
            curs.execute("""INSERT into PIR1 values (%s,%s)""",(z,path))
            db.commit()
        print("Data Saved to Database")
	fromaddr = "sender@gmail.com" #EMAIL SECTION
	toaddr = "receiver@money-wizards.com"
	msg = MIMEMultipart()
	msg['From'] = fromaddr
	msg['To'] = toaddr
        msg['Subject'] = "INTRUDER ALERT"
	body = "PFA the attachment of the INTRUDER at PIR1 @ "+str(z)
	msg.attach(MIMEText(body, 'plain'))
	filename = str(z)+".jpg"
	attachment = open('/var/www/html/Intruder_Images/%s.jpg'%str(z), "rb")
	part = MIMEBase('application', 'octet-stream')
	part.set_payload((attachment).read())
	encoders.encode_base64(part)
	part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
	msg.attach(part)
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(fromaddr, "tyeppassword")
	text = msg.as_string()
	server.sendmail(fromaddr, toaddr, text)
	server.quit()
	print("CHECK YOUR MAIL FOR THE ATTACHMENT OF THE INTRUDER")
	GPIO.output(buz,GPIO.LOW)
