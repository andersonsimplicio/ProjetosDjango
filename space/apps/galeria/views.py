from django.shortcuts import render
from .models import Fotografia



def index(request):
    fotografias= Fotografia.objects.order_by("date").filter(publicada=True)
    
    
    return render(request, 'home.html',{"cards":fotografias})

def imagem(request,foto_id):
    fotografia = Fotografia.objects.get(pk=foto_id)
    return render(request, 'imagem.html',{"fotografia":fotografia})