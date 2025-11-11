#  Sistema de Inscrição com Geração e Envio de Convite Personalizado

# Sobre o projeto
Uma aplicação web que permite a inscrição de usuários em um evento e envia automaticamente
um convite personalizado por e-mail, com o nome do participante impresso na imagem do convite.
  

## Layout web
![Web 1](https://github.com/GuilhermeGTM/Envia_convite_Email_Assincrono/blob/main/img_git/imagem/1.png)

![Web 2](https://github.com/GuilhermeGTM/Envia_convite_Email_Assincrono/blob/main/img_git/imagem/2.png)

![Web 3](https://github.com/GuilhermeGTM/Envia_convite_Email_Assincrono/blob/main/img_git/imagem/3.png)

![Web 4](https://github.com/GuilhermeGTM/Envia_convite_Email_Assincrono/blob/main/img_git/imagem/4.png)


# 🧰 Tecnologias Utilizadas

| Tecnologia    | Finalidade                                                                 |
|---------------|----------------------------------------------------------------------------|
| **Python**    | Linguagem principal para backend e automações                              |
| **Django**    | Framework web para estruturação do projeto e gerenciamento de modelos/views|
| **Celery**    | Gerenciamento de tarefas assíncronas (envio de e-mails em background)      |
| **Redis**     | Broker para fila de tarefas do Celery                                      |
| **Pillow (PIL)** | Manipulação de imagens para gerar convites personalizados              |
| **SMTP (Email)** | Envio de e-mails com imagem embutida no corpo                          |
| **HTML/CSS**  | Formatação do corpo do e-mail com layout visual                            |



## DB
- SQLite3

## 🧠 Funcionalidades

- **Formulário de inscrição**  
  Interface simples para o usuário informar nome e e-mail.

- **Persistência de dados**  
  Armazena os dados do inscrito em um modelo `Pessoa`.

- **Geração de convite**
  - Utiliza uma imagem base (`convite.png`) como template.
  - Escreve o nome do participante na imagem usando Pillow.
  - Salva o convite em `media/convites/{token}.png` com nome criptografado.

- **Envio automático de e-mail**
  - E-mail enviado via Celery para não bloquear a requisição.
  - Corpo do e-mail em HTML com imagem embutida (`cid`) para visualização direta.
  - Alternativa de envio com imagem como anexo também 

# Como executar o projeto

```bash
instalar o venv na pasta do projeto
--->python -m venv .venv
ativando venv
--->.\.venv\Scripts\Activate
baixando as dependencias
--->python -m pip install -r requirements.txt
--->python manage.py migrate
-->python manage.py runserver
```

# Autor

Guilherme Timm Moreira

