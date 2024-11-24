import smtplib
import ssl
from email.message import EmailMessage
import logging

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def send_email(from_email: str, to_email: str, subject: str, body: str, password_file: str) -> None:
    """Envia um e-mail com os parâmetros fornecidos."""
    try:
        # Ler a senha
        with open(password_file, "r") as f:
            password = f.read().strip()
        if not password:
            raise ValueError("Senha não pode estar vazia.")

        # Configurar mensagem
        message = EmailMessage()
        message["From"] = from_email
        message["To"] = to_email
        message["Subject"] = subject
        message.set_content(body)

        # Conexão segura com o servidor SMTP
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
            smtp.login(from_email, password)
            smtp.sendmail(from_email, to_email, message.as_string())

        # Log ao enviar com sucesso
        logging.info("E-mail enviado com sucesso para %s", to_email)

    except Exception as e:
        # Log para erros
        logging.error("Erro ao enviar o e-mail: %s", e)

if __name__ == "__main__":
    # Dados do e-mail
    from_email = "t06226743@gmail.com"
    to_email = "t06226743@gmail.com"
    subject = "Curso Python"
    body = '''
    A melhor forma de prever o futuro é criá-lo.
    Aprendendo a linguagem Python
    '''
    password_file = "senha"

    send_email(from_email, to_email, subject, body, password_file)
