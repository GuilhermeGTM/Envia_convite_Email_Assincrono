from django.shortcuts import render
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import Pessoa
from .tasks import cria_convite

def inscricao(request):
    return render(request, 'inscricao.html')


def processa_inscricao(request):
    if request.method == 'POST':
        nome = request.POST.get('nome', '').strip()
        email = request.POST.get('email', '').strip()

        erros = []

        # Validação do nome
        if not nome:
            erros.append("O nome é obrigatório.")

        # Validação do e-mail
        if not email:
            erros.append("O e-mail é obrigatório.")
        else:
            try:
                validate_email(email)
            except ValidationError:
                erros.append("O e-mail informado não é válido.")

        # Se houver erros, retorna para o formulário com mensagens
        if erros:
            return render(request, 'inscricao.html', {'erros': erros, 'nome': nome, 'email': email})

        # Salva e dispara tarefa
        pessoa = Pessoa(nome=nome, email=email)
        pessoa.save()
        cria_convite.delay(nome, email)

        return render(request, 'cadastro_confirmado.html')

    return render(request, 'inscricao.html')
