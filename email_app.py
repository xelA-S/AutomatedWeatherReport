import smtplib
import ssl  # secure socket layer
from email.message import EmailMessage
from weather import current_weather
import schedule
import time


start_code_password = input("Enter your password: ")


def verify():
    sender_email = "justtestingautomation@gmail.com"
    email_password = start_code_password
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        return server.login(sender_email, email_password)


try:
    verify()
except Exception:
    print("Invalid password. Please Try Again.")


def WeatherReport():
    sender_email = "justtestingautomation@gmail.com"
    reciever_email = "asmith6398@gmail.com"
    email_password = start_code_password

    subject = "Daily Weather Report"
    body = current_weather("london")


    message = EmailMessage()

    message["From"] = sender_email
    message["To"] = reciever_email
    message["Subject"] = subject
    message.set_content(body)

    # this is used to create a secure connection when connecting to gmail when using smtplib
    context = ssl.create_default_context()

    print("Sending Email")
    # this creates the SSL server,connecting to the gmail server, using port 465 and using the "context" defined above
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, email_password)
        server.sendmail(sender_email, reciever_email, message.as_string())

    print("Email Sent!")


schedule.every().day.at("08:00").do(WeatherReport)


while True:
    schedule.run_pending()
    time.sleep(1)
