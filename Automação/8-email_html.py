from email.message import EmailMessage
import smtplib
import ssl
import mimetypes
import logging

# Configuração básica do log
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]  # Exibe no console
)

# Carregar credenciais e conteúdo do e-mail
password = open('files/senha', 'r').read()
from_email = 't06226743@gmail.com'
to_email = 't06226743@gmail.com'
subject = 'Proposta Parceria Personalizada'
body = open('files/index.html.txt', 'r', encoding='utf-8').read()

# Configuração da mensagem
message = EmailMessage()
message['From'] = from_email
message['To'] = to_email
message['Subject'] = subject
message.set_content(body, subtype='html')

# Configuração SSL
safe = ssl.create_default_context()

# Adicionar anexo
anexo = 'files/texto.txt'
try:
    mime_type, mime_subtype = mimetypes.guess_type(anexo)[0].split('/')
    with open(anexo, 'rb') as a:
        message.add_attachment(
            a.read(),
            maintype=mime_type,
            subtype=mime_subtype,
            filename=anexo
        )
    logging.info(f"Anexo '{anexo}' adicionado com sucesso.")
except Exception as e:
    logging.error(f"Erro ao anexar o arquivo '{anexo}': {e}")
    raise

# Enviar o e-mail
try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=safe) as smtp:
        smtp.login(from_email, password)
        smtp.sendmail(from_email, to_email, message.as_string())
    logging.info("E-mail enviado com sucesso!")
except Exception as e:
    logging.error(f"Erro ao enviar e-mail: {e}")
    raise
