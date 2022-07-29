import smtplib #smtp library
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.message import EmailMessage
# import os #to get environment varibles

email_user = 'digiworldy2k@gmail.com'
email_passowrd = 'ugputgreuvsovtsp'

email = pd.read_excel("C:/Users/user/Desktop/git/py/100dayscd/work2.xlsx")
emails = email["mails"].values



with smtplib.SMTP('smtp.gmail.com', 587) as smtp: #connect to the gmail account we are using
    smtp.ehlo() #identify with the server we are using
    smtp.starttls()  #to encrypt our traffic we use this line
    smtp.ehlo() #to reidentify our selves as a encrypted password

    smtp.login(email_user, email_passowrd) #to login to our mail server

    subject  = "hello proff"
    body = "Hope you had a nice time at work today" #create our body and msg for email

    msg = f'Subject {subject}\n\n{body}' 

    smtp.sendmail(email_user, emails , msg)