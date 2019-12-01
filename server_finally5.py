import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import RPi.GPIO as GPIO
from subprocess import call
import picamera
import os
import sys
import time
import datetime
import smtplib


def record():
        camera = picamera.PiCamera()
        camera.resolution = (1280, 720)
        camera.framerate = 60
        now = datetime.datetime.now()
        filename = now.strftime('%Y-%m-%d %H:%M:%S')
        camera.start_recording(output = filename + '.h264')
        camera.wait_recording(5)
        camera.stop_recording()
	camera.close()
	email_user = 'son33620812@gmail.com'
	email_password = 'hlove3308'
	email_send = 'son33620812@gmail.com'
	subject = 'project finish??'

	msg = MIMEMultipart()
	msg['From'] = email_user
	msg['To'] = email_send
	msg['Subject'] = subject


	body = 'project finish~~'
	msg.attach(MIMEText(body,'plain'))

	attachment  =open(filename+".h264",'rb')

	part = MIMEBase('application','octet-stream')
	part.set_payload((attachment).read())
	encoders.encode_base64(part)
	part.add_header('Content-Disposition',"attachment; filename= "+filename)
	msg.attach(part)


	text = msg.as_string()
	server = smtplib.SMTP('smtp.gmail.com',587)
	server.starttls()

	server.login(email_user,email_password)
	server.sendmail(email_user,email_send,text)
	server.quit()

GPIOIN = 17
GPIOOUT = 27
GPIO.setmode(GPIO.BCM)
print("HC-SR501 motion detection start")
GPIO.setup(GPIOIN, GPIO.IN)
GPIO.setup(GPIOOUT, GPIO.OUT)


try:
        while True:
            	state = GPIO.input(GPIOIN)
    		
	    	if (state == True):
			print("motion detected")
			breakAll = 0
			
			while (breakAll == 0):
        			if (state == False):
					print("motion not detected")
					startTime = time.time()
					
        				while (breakAll == 0):
						print("motion not detected")
            					nowTime = time.time()
            					if (nowTime - startTime >= 10):
                					record()
                					breakAll = 1
						time.sleep(0.5)
							
				if (breakAll == 1):
					break
		else:
			print("motion not detected")
					
		GPIO.output(GPIOOUT, state)
		time.sleep(0.5)

except KeyboardInterrupt:
        GPIO.cleanup()
