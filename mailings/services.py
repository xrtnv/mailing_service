import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



from config.settings import SMTP_SERVER, FROM_MAIL, MAIL_KEY


def send_mail(_to_mail, _subject ,_message):
    msg = MIMEMultipart()

    to_email = _to_mail
    message = _message

    msg.attach(MIMEText(message, 'plain'))
    msg['Subject'] = _subject

    server = SMTP_SERVER
    server.starttls()
    server.login(FROM_MAIL, MAIL_KEY)
    server.sendmail(FROM_MAIL, to_email, msg.as_string())
    server.quit()




