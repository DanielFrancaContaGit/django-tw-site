from django.shortcuts import render
from core.models import Produtos, Home
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.views.decorators.csrf import csrf_protect
from django.urls import reverse

def home_view(request):

    produtos = Produtos.objects.values()

    if request.method == "POST":

        name = request.POST['name']
        description = request.POST['description']
        url = request.POST['url']

        novo_produto = Produtos()

        novo_produto.name = name
        novo_produto.url = url
        novo_produto.description = description

        novo_produto.save()

        return render(request, 'components/productSection.html', {
            'produtos': produtos
        })

    
    if Home.objects.values():
        home = Home.objects.values()[0]
    else:
        home = { 'title': 'mude em /admin', 'sub_title': 'mude en /admin' }    

    return render(request, 'pages/home.html', {
            'home': home, 
            'produtos': produtos
        })

@csrf_protect
def homedelete(request):

    # produtos = Produtos.objects.values()

    produtos = [{
         "url": "data:image/jpeg;base64,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",
         "name": "coxinha",
         "description": "coxinha de massa de batata",
     }]

    return render(request, 'components/productcard.html', {
           'produtos': produtos
        })
