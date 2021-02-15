from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.template import loader
from django.http import HttpResponse

from .models import Produto


def index(request):
    # lista todas as instancias da class Produto, importada acima
    produtos = Produto.objects.all()

    # request.user retorna o usuario logado
    if str(request.user) == 'AnonymousUser':
        teste = 'Usuário NÃO Logado'
    else:
        teste = f'Usuário LOGADO:{request.user}'

    context = {
        'curso'   : 'Primeiro teste Django',
        'outro'   : 'Dicionario "context" dentro em views.index.py',
        'logado'  : teste,
        'produtos': produtos
    }
    return render(request, 'index.html', context)


def produto(request, pk):
    # produtopk = Produto.objects.get(id=pk)
    produtopk = get_object_or_404(Produto, id=pk)

    context = {
        'produto': produtopk
    }

    return render(request, 'produto.html', context)


def usuarios(request):
    return render(request, 'usuarios.html')


def error404(request, exception):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)


def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)
