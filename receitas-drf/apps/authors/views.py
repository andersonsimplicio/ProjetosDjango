from django.http import Http404
from django.shortcuts import redirect, render
from django.contrib import messages
from apps.authors.forms import RegisterForms,LoginForm
from django.urls import reverse


# Create your views here.
def register_view(request):   
    request.session['number'] = request.session.get('number')+1 if request.session.get('number') else 1
    
    register_form_data = request.session.get('register_form_data',None)
    if register_form_data:
        form = RegisterForms(register_form_data)
    else:
        form = RegisterForms()
        
    context = {
        'form':form,
        'form_action': reverse('apps.authors:register_create')
    }
    
    return render(request, 'authors/pages/register_view.html',context=context)

def register_create(request):   
    
    if not request.POST:
        raise Http404()
    POST = request.POST
    request.session['register_form_data'] = POST
    form = RegisterForms(request.POST)  
    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()
        messages.success(request, 'Seu usuário foi criado, faça o login.')
        del(request.session['register_form_data'])  
    context = {
        'form':form,
        'form_action':reverse('apps.authors:login_create')
    }
    
    return redirect('apps.authors:register') 

def login_view(request):
    form = LoginForm()
    context = {
        'form':form,
    }
    return render(request,'authors/pages/login.html',context)


def login_create(request):
    
    return render(request,'authors/pages/login.html')