from django.shortcuts import render
from core.models import Produtos, Home

def home_view(request):

    produtos = Produtos.objects.values()
    home = Home.objects.values()[0]

    return render(request, 'pages/home.html', {
            'home': home, 
            'produtos': produtos
        })
