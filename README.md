# Mailer Automático

Script em Python para envio automatizado de e-mails com anexo (currículo) para uma lista de contatos.  
As credenciais e configurações são armazenadas em um arquivo `.env` para maior segurança.

---

## 📦 Pré-requisitos

- Python 3.8 ou superior
- Pip (gerenciador de pacotes do Python)
- Conta de e-mail com acesso SMTP (Gmail, Outlook, etc.)
- Senha de App configurada (no caso do Gmail)

---

## ⚙️ Configuração do Ambiente

1. **Clonar o repositório**
```bash
git clone https://github.com/seuusuario/mailer.git
cd mailer
```

2. **Criar e configurar o arquivo .env**
Crie um arquivo .env na raiz do projeto com o seguinte conteúdo:

```bash
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
EMAIL=seuemail@gmail.com
PASSWORD=sua_senha_de_app
CSV_PATH=contatos.csv
ATTACHMENT_PATH=Lucas_Ferreira_Curriculo.pdf
```

3. **Instalar as dependências**
```bash
pip install -r requirements.txt
```

---


## 📄 Formato do CSV de Contatos
O arquivo CSV deve estar no formato:

```bash
nome,email
João da Silva,joao@empresa.com
Maria Souza,maria@empresa.com
```

## 🚀 Executando o Script
Para executar o script:

```bash
python mailer.py
```
