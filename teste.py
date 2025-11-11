import smtplib

server = smtplib.SMTP_SSL('smtp.titan.email', 465)
server.login('teste@micheladomingues.com', 'Petu#3060')
server.sendmail(
    'teste@micheladomingues.com',
    'guilherme-gtm@hotmail.com',
    'Subject: Teste\n\nMensagem de teste'
)
server.quit()