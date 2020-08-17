from django.shortcuts import render, get_object_or_404, redirect
from receitas.models import Receita

def busca(request):
    lista_receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if busca:
            lista_receitas = lista_receitas.filter(nome_receita__icontains=nome_a_buscar)

    dados = {
        'receitas': lista_receitas
    }

    return render(request, 'receitas/buscar.html', dados)