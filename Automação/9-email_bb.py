from email.message import EmailMessage
import smtplib
import ssl
import mimetypes

# Credenciais e configuração do e-mail
password = open('files/senha', 'r').read()
from_email = 't06226743@gmail.com'
to_email = 't06226743@gmail.com'
subject = 'Informes BB'
body = open('files/fato_bb.txt', 'r', encoding='utf-8').read()

# Criação da mensagem
message = EmailMessage()
message['From'] = from_email
message['To'] = to_email
message['Subject'] = subject
message.set_content(body)

# Contexto seguro
safe = ssl.create_default_context()

# Adicionando o primeiro anexo
anexo1 = 'bb_preco.png'
mime_type1, mime_subtype1 = mimetypes.guess_type(anexo1)[0].split('/')
with open(anexo1, 'rb') as a1:
    message.add_attachment(
        a1.read(),
        maintype=mime_type1,
        subtype=mime_subtype1,
        filename=anexo1
    )

# Adicionando o segundo anexo
anexo2 = 'bb_volume.png'
mime_type2, mime_subtype2 = mimetypes.guess_type(anexo2)[0].split('/')
with open(anexo2, 'rb') as a2:
    message.add_attachment(
        a2.read(),
        maintype=mime_type2,
        subtype=mime_subtype2,
        filename=anexo2
    )

# Envio do e-mail
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=safe) as smtp:
    smtp.login(from_email, password)
    smtp.sendmail(from_email, to_email, message.as_string())
