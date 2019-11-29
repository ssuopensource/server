import smtplib
import sys

from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo()
smtpserver.login('son33620812@gmail.com', 'hlove3308')

sys.path.append('/your/dir/to/tensorflow/models')
sys.path.append('/your/dir/to/tensorflow/models/slim')


me = 'son33620812@gmail.com'
you = 'dudals57824318@gmail.com'
user = 'son33620812'
passwd = 'hlove3308'
smtp_server = 'smtp.gmail.com'
smtp_port = 465


msg = MIMEMultipart()
msg['Subject'] = 'Hi'


msg['From'] = me
msg['To'] = you
msg.preamble = 'practice'


fp = open('v.jpg', 'rb')
img = MIMEImage(fp.read())
fp.close()
msg.attach(img)


s = smtplib.SMTP('localhost')
s.sendmail(me, you, msg.as_string())
s.quit()

s = smtplib.SMTP_SSL('smtp.gmail.com',465)
s.login(user, passwd)
s.sendmail(me, you, msg.as_string())
s.quit()
