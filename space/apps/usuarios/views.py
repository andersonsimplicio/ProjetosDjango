from django.shortcuts import render,redirect
from .froms import LoginForms,CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

def login(request):
    form = LoginForms()
    if request.method == "POST":
        form = LoginForms(request.POST)
        if form.is_valid():
            nome = form['nome_login'].value()
            senha = form['senha'].value()
            usuario = auth.authenticate(
                request,
                username=nome,
                password=senha
            )
            print(usuario)
            if usuario is not None:
                messages.success(request,f"Usuario:{nome} Logado com sucesso")
                auth.login(request,usuario)
                return redirect('home')
            else:
                messages.error(request,f"Erro em efetuar login")
                return redirect('login')

    return render(request,"login.html",{"form":form})


def cadastro(request):
    form =  CadastroForms() 
    if request.method == "POST":
        form = CadastroForms(request.POST)
        if form.is_valid():
            nome = form['nome_cadastro'].value()
            email = form['email'].value()
            senha = form['senha1'].value()

            if User.objects.filter(username=nome).exists():
                messages.error(request,f"Usuário já cadastrado")
                return redirect('cadastro')
            usuario = User.objects.create_user(email=email,username=nome,password=senha)
            usuario.save()
            messages.success(request,f"Cadastro realizado com sucesso!")
            return redirect('login')

    
    return render(request,"cadastro.html",{"form":form})


def logout(request):
    auth.logout(request)
    messages.success(request,"Até logo")
    return redirect('login')