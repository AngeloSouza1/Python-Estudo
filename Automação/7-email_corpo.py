from email.message import EmailMessage
import smtplib
import ssl
import logging

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

try:
    # Carregar senha
    with open("senha", "r") as f:
        password = f.read().strip()
    if not password:
        raise ValueError("Senha não pode estar vazia.")

    # Dados do e-mail
    from_email = "t06226743@gmail.com"
    to_emails = ["t06226743@gmail.com", "angeloafdesouza@gmail.com"]  # Lista de destinatários
    subject = "Proposta Parceria"
    with open("files/texto.txt", "r", encoding="utf-8") as f:
        body = f.read()

    # Configurar mensagem
    message = EmailMessage()
    message["From"] = from_email
    message["To"] = ", ".join(to_emails)  # Adiciona todos os destinatários no cabeçalho "To"
    message["Subject"] = subject
    message.set_content(body)

    # Conexão segura com o servidor SMTP
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(from_email, password)
        smtp.sendmail(from_email, to_emails, message.as_string())  # Envia para todos os destinatários
        # Log após o envio do e-mail
        logging.info("E-mail enviado com sucesso para: %s", ", ".join(to_emails))

except Exception as e:
    # Log para erros
    logging.error("Erro ao enviar e-mail: %s", e)
