from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Fotografia
from .forms import FotografiaForms
from django.contrib import messages


def index(request):
    fotografias= Fotografia.objects.order_by("date").filter(publicada=True)
    context = {
        "cards": fotografias,
        "user": request.user  # Adiciona o usuário ao contexto
    }
        
    return render(request, 'home.html',context)

def imagem(request,foto_id):
    fotografia = Fotografia.objects.get(pk=foto_id)
    context = {
        "fotografia":fotografia,
        "user": request.user  # Adiciona o usuário ao contexto
    }
    return render(request, 'imagem.html',context)

def buscar(request):
    fotografias= Fotografia.objects.order_by("date").filter(publicada=True)
    if "buscar" in request.POST:
        nome_a_buscar = request.POST["buscar"]
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)
    return render(request, 'buscar.html',{"cards":fotografias})

@login_required
def nova_image(request):
    form = FotografiaForms(initial={'usuario': request.user.username})  
    
    if request.method == "POST":
        form = FotografiaForms(request.POST,request.FILES)
        if form.is_valid():
            messages.success(request,"Nova fotografia cadastrada")
            #form.save()
            return redirect('home')
        else:
            messages.error(request,"Erro ao cadastrar")
            print(form.errors)
    
    return render(request, 'nova_imagem.html',{"form":form,"user":request.user})

@login_required
def editar_image(request):

     return render(request, 'editar_imagem.html',{})

@login_required
def deletar_image(request):

     return render(request, 'deletar_imagem.html',{})