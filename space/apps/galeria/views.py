from django.shortcuts import render

def index(request):
    return render(request, 'home.html')

def imagem(request):
    return render(request, 'imagem.html')