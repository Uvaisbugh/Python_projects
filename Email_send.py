#email sender
from email.message import EmailMessage
import smtplib
import ssl

email_sender = 'email@gmail.com'
email_password = 'password'
email_receiver = 'receiver@gmail.com'

subject = input("Subject: ")
body = input("Body: ")

#initialize email
msg = EmailMessage()
msg['Subject'] = subject
msg['From'] = "Sender"
msg['To'] = "Receiver"
msg.set_content(body)

#send email
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login('email', 'password')
    smtp.sendmail(email_sender, email_receiver, msg.as_string())
    print("Email sent")
    