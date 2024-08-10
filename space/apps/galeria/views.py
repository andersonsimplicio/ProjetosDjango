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
    if fotografia.usuario is not None:
        autor = request.user.id == fotografia.usuario.id
    else:
        autor =False
    context = {
        "fotografia":fotografia,
        "user": request.user, # Adiciona o usuário ao contexto
        "autor":autor
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
        form.data = form.data.copy()
        form.data['usuario'] =request.user.id
        if form.is_valid():
            messages.success(request,"Nova fotografia cadastrada")
            form.save()
            return redirect('home')
        else:
            messages.error(request,f"{form.errors.as_text()}")
           
    
    return render(request, 'nova_imagem.html',{"form":form,"user":request.user})

@login_required
def editar_image(request,foto_id):
    foto = Fotografia.objects.get(pk=foto_id)
    form = FotografiaForms(instance=foto,initial={'usuario': request.user.username})
    context = {
         "form":form,
         "user":request.user.username,
         "foto_id":foto_id,
     }
    if request.method == 'POST':
        form = FotografiaForms(request.POST,request.FILES,instance=foto)
        form.data = form.data.copy()
        form.data['usuario'] =request.user.id
        if form.is_valid():  
            messages.success(request,"Fotografia editada com sucesso")
            form.save()
            return redirect('home')
        else:
            messages.error(request,f"{form.errors.as_text()}")
         
    return render(request, 'editar_imagem.html',context)

@login_required
def deletar_image(request,foto_id):
    foto = Fotografia.objects.get(pk=foto_id)
    foto.delete()
    messages.success(request,"Fotografia apagada com sucesso!")
    return redirect('home')

def filtro(request,categoria):
    fotografias= Fotografia.objects.order_by("date").filter(publicada=True,categoria=categoria)

    context = {
        "cards": fotografias,
        "user": request.user  # Adiciona o usuário ao contexto
    }
        
    return render(request, 'home.html',context)