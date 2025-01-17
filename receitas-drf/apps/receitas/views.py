from django import views
from django.shortcuts import render,get_list_or_404, get_object_or_404
from django.http import Http404
from django.http.response import Http404
from .models import Receita
from django.db.models import Q

def home(request):
    recipes = Receita.objects.filter(
        is_published=True
    ).order_by('-id')
  
    context = {
        'title':'Home',
        'receitas': recipes,
    }    
    
    return render(request,'receitas/pages/home.html',context)

def receita(request,id:int):
    receita =get_object_or_404(Receita, pk=id, is_published=True,)
    
    context = {
        'title':'Detalhes',
        'receita': receita ,
        'is_detail_page': True,
    }
    return render(request,'receitas/pages/receita-detalhes.html',context)

def categoria(request,category_id):
    recipes = get_list_or_404(
        Receita.objects.filter(
            category__id=category_id,
            is_published=True,
        ).order_by('-id')
    )
    
    if not recipes:
        raise Http404('Not found 🥲')
    
    return render(request,'receitas/pages/categoria.html',context={'receitas': recipes, 'title': f'{recipes[0].category.name} - Categoria'})

def search(request):
    search_term = request.GET.get('q', '').strip()
    
    if not search_term:
        raise Http404("Você deve fornecer um termo de busca.")    
    receitas = Receita.objects.filter(  
        Q(
            Q(title__icontains=search_term) |
            Q(description__icontains=search_term),
        ),
        is_published=True)
    
    context = {
                   'page_title': f'Busca por "{search_term}" ',
                   'search_term': search_term,
                   'receitas':receitas,
                   }
    return render(request, 'receitas/pages/search.html',context)