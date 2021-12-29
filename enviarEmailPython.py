import pandas as pd 
tabela_emails = pd.read_excel('/content/drive/MyDrive/Colab Notebooks/emails.xlsx')
display(tabela_emails)

def enviar_email(nome, gmail):
  import smtplib
  import email.message

  server = smtplib.SMTP('smtp.gmail.com:587')
  corpo_email = f"""
  <p> Caro, {nome} </p>
  <p> Aqui está a tabela de vendas desse mês </p>
  <p> https://drive.google.com/file/d/1dedVJdioJS00wCeaAOKNgGAU4Gj_THMB/view?usp=sharing </p>
  """
…  password = "colocar aqui"
  msg.add_header('Content-Type', 'text/html')
  msg.set_payload(corpo_email )

  s = smtplib.SMTP('smtp.gmail.com: 587')
  s.starttls()
  # Login Credentials for sending the mail
  s.login(msg['From'], password)
  s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
  print('Email enviado')

emails = tabela_emails['email']
nome = tabela_emails['Nome']
for i in range(0,len(tabela_emails['Nome'])):
  enviar_email(nome[i], emails[i])


