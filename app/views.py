from django.shortcuts import render
from core.models import Produtos, Home
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.views.decorators.csrf import csrf_protect
from django.urls import reverse

def home_view(request):

    if request.method == "POST":
        name = request.POST['name']
        description = request.POST['description']
        url = request.POST['url']

        novo_produto = Produtos()

        novo_produto.name = name
        novo_produto.url = url
        novo_produto.description = description

        novo_produto.save()

    produtos = Produtos.objects.values()

    if Home.objects.values():
        home = Home.objects.values()[0]
    else:
        home = { 'title': 'mude em /admin', 'sub_title': 'mude en /admin' }    

    return render(request, 'pages/home.html', {
            'home': home, 
            'produtos': produtos
        })

@csrf_protect
def home(request):

    name = request.POST['name']
    description = request.POST['description']
    url = request.POST['url']

    novo_produto = Produtos()

    novo_produto.name = name
    novo_produto.url = url
    novo_produto.description = description

    novo_produto.save()

    return HttpResponseRedirect(' ')



