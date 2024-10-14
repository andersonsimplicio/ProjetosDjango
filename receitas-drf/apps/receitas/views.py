from django.shortcuts import render
from utils.receitas.farm import make_recipe

def home(request):
    context = {
        'title':'Home',
        'receitas': [make_recipe() for _ in range(10)],
    }
    return render(request,'receitas/pages/home.html',context)

def receita(request,id:int):
    context = {
        'title':'Detalhes',
        'receita': make_recipe(),
        'is_detail_page': True,
    }
    return render(request,'receitas/pages/receita-detalhes.html',context)
