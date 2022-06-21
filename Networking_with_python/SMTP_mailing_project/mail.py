#This python script enables you to send mail via Python

#Importing smtp library
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP('smtp.gmail.com', 587) #Getting the stmp address of gmail

server.ehlo() # starting the server
server.starttls()

with open('password.txt', 'r') as f:
    password = f.read()

server.login('olawale@gmail.com', password)

msg = MIMEMultipart()
msg['From'] = 'Hammed Babatunde Idris'
msg['To'] = 'olawale@gmail.com'
msg['Cc'] = ''
msg['Bcc'] = ''
msg['Subject'] = 'Just A test'

with open('message.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

##Attaching and Decoding image
filename = 'python.jpeg'
attachment = open(filename, 'rb')
p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())
encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}')

# Attaching the image to the message
msg.attach(p)

text = msg.as_string()
server.sendmail('olawale@gmail.com', 'olawale@gmail.com', text) #sending the mail

