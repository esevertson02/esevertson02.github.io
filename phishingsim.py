import smtplib
from email.mime.text import MIMEText

subject = "Balls"
body = "Hey there, you're fired"
sender = "rlikamwaa@gmail.com"
recipients = ["ndander7@asu.edu"]
password = "uoghvcadcskgibsr"


def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body, 'html')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(sender, password)
        smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Message sent!")


send_email(subject, body, sender, recipients, password)
