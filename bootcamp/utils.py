from bootcamp import app, mail
from flask_mail import Message


def send_email(to, subject, template):
    msg = Message(
        subject,
        recipients=[to],
        html=template,
        sender='TechCap Initiative'
    )
    mail.send(msg)