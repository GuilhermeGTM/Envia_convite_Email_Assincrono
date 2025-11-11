from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from email.mime.image import MIMEImage
from PIL import Image, ImageDraw, ImageFont
from hashlib import sha256
import os

@shared_task
def cria_convite(nome, email):  
    # GERA O CONVITE
    template = os.path.join(settings.STATIC_ROOT, 'img/convite.png')
    img = Image.open(template)
    img_escrever = ImageDraw.Draw(img)
    fonte = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", size=30)
    img_escrever.text((32, 180), nome, fill=(0, 0, 0), font=fonte)

    chave_secreta = "UHASUYGAs786876A7S654@@#@#!@#!@auhydgwua2y123AWDNUI1233354"
    token = sha256((email + chave_secreta).encode()).hexdigest()
    path_salvar = os.path.join(settings.MEDIA_ROOT, f'convites/{token}.png')
    img.save(path_salvar)

    # ENVIA O EMAIL COM IMAGEM EMBUTIDA
    subject = 'Confirmação de inscrição'
    from_email = 'seu_email'
    to = [email]
    text_content = 'Sua inscrição foi confirmada! Veja o convite abaixo.'

    html_content = f'''
        <p>Olá {nome},</p>
        <p>Sua inscrição foi confirmada com sucesso!</p>
        <p>Aqui está seu convite personalizado:</p>
        <p><img src="cid:convite_inline"></p>
        <p>Nos vemos lá!</p>
    '''

    email_message = EmailMultiAlternatives(subject, text_content, from_email, to)
    email_message.attach_alternative(html_content, "text/html")

    # Embute a imagem no corpo do e-mail
    with open(path_salvar, 'rb') as img_file:
        mime_image = MIMEImage(img_file.read())
        mime_image.add_header('Content-ID', '<convite_inline>')
        mime_image.add_header('Content-Disposition', 'inline', filename=f'convite_{nome}.png')
        email_message.attach(mime_image)

    email_message.send()











"""
from celery import shared_task
#email
from django.core.mail import send_mail
#pillow
import PIL
from PIL import Image, ImageDraw, ImageFont
from django.conf import settings
import os
#geradodor de rash
from hashlib import sha256

@shared_task
def cria_convite(nome, email):  

    # CRIA O CONVITE
   
    template = os.path.join(settings.STATIC_ROOT, 'img/convite.png')
    img = Image.open(template) # abre a imagen no diretorio acima
    img_escrever = ImageDraw.Draw(img) # escreve na imagen
    fonte = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", size=40) #ajusta fonte
    img_escrever.text((79, 165), nome, fill=(0, 0, 0), font=fonte) # padrão de cor e onde vai escrever
    #token para salvar o nome da imagem
    chave_secreta = "UHASUYGAs786876A7S654@@#@#!@#!@auhydgwua2y123AWDNUI1233354"
    token = sha256((email + chave_secreta).encode()).hexdigest()
    path_salvar = os.path.join(settings.MEDIA_ROOT, f'convites/{token}.png')
    img.save(path_salvar)

    # ENVIA O EMAIL
    send_mail(
    subject='Confirmação de inscrição',
    message=f'Sua inscrição foi processada com sucesso! (taks) \n Aqui está o link do seu convite: http://127.0.0.1:8000/media/convites/{token}.png',
    from_email='teste@micheladomingues.com',
    recipient_list=[email],
    )
"""