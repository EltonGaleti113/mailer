import smtplib
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import time
import os
from dotenv import load_dotenv

load_dotenv()

SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT"))
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

contatos = pd.read_csv("contatos.csv")

with open("curriculo.pdf", "rb") as f:
    curriculo_pdf = f.read()

for index, row in contatos.iterrows():
    nomeUsuario = input("Qual seu nome: ")
    nomeEmpresa = row["nome"]
    destinatario = row["email"]

    msg = MIMEMultipart()
    msg["From"] = EMAIL
    msg["To"] = destinatario
    msg["Subject"] = "Oportunidade de trabalho em TI"

    corpo = f"""
Olá {nomeEmpresa},

Meu nome é {nomeUsuario} e gostaria de manifestar meu interesse em integrar a equipe {nomeEmpresa}, atuando como Desenvolvedor ou na área de Suporte de TI.

Possuo mais de três anos de experiência na área de tecnologia, com sólida atuação no desenvolvimento web (Laravel, Angular, Spring Boot), manutenção de sistemas, diagnóstico e resolução de problemas técnicos. Também tenho experiência com bancos de dados SQL, infraestrutura de TI, Docker, Git/GitHub e boas práticas de segurança da informação.

Sou graduando em Ciências da Computação e me destaco pela proatividade, comunicação eficiente e comprometimento com resultados. Tenho certeza de que posso contribuir para a melhoria contínua dos processos e sistemas do hospital.

Segue em anexo meu currículo e carta de apresentação para avaliação.

Agradeço desde já pela atenção e coloco-me à disposição para entrevistas e esclarecimentos.

Atenciosamente,
{nomeUsuario}
📧 egaleti2003@gmail.com
📱 +55 (17) 99218-6552
🔗 GitHub: https://github.com/EltonGaleti113
👨 Linkedin: https://www.linkedin.com/in/elton-galeti-6ab11a2a7/
    """

    msg.attach(MIMEText(corpo, "plain"))

    anexo = MIMEApplication(curriculo_pdf, _subtype="pdf")
    anexo.add_header(
        "Content-Disposition",
        "attachment",
        filename="Desenvolvedor_web_Elton_Pt-br.pdf",
    )
    msg.attach(anexo)

    # Envio
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL, PASSWORD)
        server.send_message(msg)

    print(f"E-mail enviado para {destinatario}")
    time.sleep(5)
