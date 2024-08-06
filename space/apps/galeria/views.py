from django.shortcuts import render
from .models import Fotografia



def index(request):
    fotografias= Fotografia.objects.order_by("date").filter(publicada=True)
    
    
    return render(request, 'home.html',{"cards":fotografias})

def imagem(request,foto_id):
    fotografia = Fotografia.objects.get(pk=foto_id)
    return render(request, 'imagem.html',{"fotografia":fotografia})

def buscar(request):
    fotografias= Fotografia.objects.order_by("date").filter(publicada=True)
    if "buscar" in request.POST:
        nome_a_buscar = request.POST["buscar"]
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)
    return render(request, 'buscar.html',{"cards":fotografias})