import os
import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "your_emailid"
    password = "generate_password"

    receiver = "reciever's_emailid"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
