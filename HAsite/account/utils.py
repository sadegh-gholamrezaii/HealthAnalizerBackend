import os.path
from pathlib import Path
from account.local_data import HOST_PASSWORD, HOST_EMAIL, HOST

BASE_DIR = Path(__file__).resolve().parent.parent


def send_email(email, message, context):
    import smtplib
    from email.message import EmailMessage
    import imghdr

    EMAIL_HOST = HOST
    EMAIL_HOST_USER = HOST_EMAIL
    EMAIL_HOST_PASSWORD = HOST_PASSWORD
    HOST_PORT_TLS = 587
    HOST_PORT_SSL = 465
    contacts = [email]

    msg = EmailMessage()
    msg['Subject'] = "Change Password"
    msg['From'] = EMAIL_HOST_USER
    msg['To'] = ', '.join(contacts)

    msg.set_content(message)
    msg.add_alternative(context, subtype='html')

    with smtplib.SMTP_SSL(EMAIL_HOST, HOST_PORT_SSL) as gmail:
        gmail.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
        gmail.send_message(msg)


def send_code(email, code):
    with open(os.path.join(BASE_DIR, 'account/email.html'), 'r') as html_file:
        html = html_file.read()
    context = html.replace("password", code)
    send_email(email=email, context=context, message=f"Your new password is {code}")
