from django.shortcuts import render

def home(request):
    context = {
        'title':'Pagina de Receitas',
        'name':'Home'
    }
    return render(request,'receitas/pages/home.html',context)
