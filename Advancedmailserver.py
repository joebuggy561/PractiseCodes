import csv
import smtplib
import pandas

# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from email.mime.base import MIMEBase
# from email import encoders
# from email.message import EmailMessage


email_user = "josephnwanijr@gmail.com"
email_password = "xmtlijkxqxnqubmg"

with open("work.csv", "rb") as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        text = ""

msg = EmailMessage()
msg['Subject'] = "Application for the role of Data Analyst/IT Support"
msg['From'] = "email_user"
msg['To'] = 'josephnwanijr@outlook.com'
msg.set_content('How is the py studies going......')# update to message from emailbox

with open('CV.pdf', 'rb') as f:
    file_data = f.read()
    file_name = f.name
    msg.add_attachment(file_data, maintype = "application", subtype = "pdf", filename = file_name)


with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(email_user, email_password)

    smtp.send_message(msg)