from django.shortcuts import render
from .froms import LoginForms,CadastroForms
def login(request):
    form = LoginForms()
    return render(request,"login.html",{"form":form})


def cadastro(request):
    form =  CadastroForms()
    return render(request,"cadastro.html",{"form":form})
