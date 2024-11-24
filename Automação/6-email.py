from email.message import EmailMessage
import smtplib
import ssl

password = open('senha', 'r').read()
from_email = 'codeti327@gmail.com'
to_email = 'codeti327@gmail.com'
subject = 'Curso Python'
body = '''
A melhor forma de prever o futuro é criá-lo.
Aprendendo a linguagem Python
'''

message = EmailMessage()
message['From'] = from_email
message['To'] = to_email
message['Subject'] = subject

message.set_content(body)
safe = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=safe) as smtp:
    smtp.login(from_email, password)
    smtp.sendmail(from_email, to_email, message.as_string())
