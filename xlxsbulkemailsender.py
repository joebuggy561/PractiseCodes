import pandas as pd
import smtplib

email = pd.read_excel("C:/Users/user/Desktop/git/py/100dayscd/work2.xlsx")
emails = email["mails"].values

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login("josephnwanijr@gmail.com", "xmtlijkxqxnqubmg")

subject  = "hello proff"
msg = "Hope you had a nice time at work today"
body = f'Subject {subject}\n\n{msg}'

for email in emails:
    server.sendmail("josephnwanijr@gmail.com", email, body)
    server.quit()