import socket
import sys
import smtplib
from email.mime.text import MIMEText

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo()
smtpserver.login('son33620812@gmail.com', 'hlove3308')

sys.path.append('/your/dir/to/tensorflow/models')
sys.path.append('/your/dir/to/tensorflow/models/slim')

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

msg = MIMEText(get_ip_address())

me = 'son33620812@gmail.com'

you = 'dudals57824318@gmail.com'


user = 'son33620812'

passwd = 'hlove3308'


smtp_server = 'smtp.gmail.com'


smtp_port = 465


msg['Subject'] = 'Hi I am suchang'


msg['From'] = me
msg['To'] = you

s = smtplib.SMTP_SSL(smtp_server, smtp_port)
s.login(user, passwd)
s.sendmail(me, you, msg.as_string())
s.quit()
