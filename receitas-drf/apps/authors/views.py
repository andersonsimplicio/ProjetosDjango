from django.http import Http404
from django.shortcuts import redirect, render
from django.contrib import messages
from apps.authors.forms import RegisterForms,LoginForm,AuthorRecipeForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from apps.receitas.models import Receita


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
        return redirect(reverse('apps.authors:login'))
    context = {
        'form':form,
        'form_action':reverse('apps.authors:login_create')
    }
    
    return redirect('apps.authors:register') 

def login_view(request):
    form = LoginForm()
    context = {
        'form':form,
        'form_action':reverse('apps.authors:login_create')
    }
    return render(request,'authors/pages/login.html',context)


def login_create(request):
    if not request.POST:
        raise Http404()
    
    form = LoginForm(request.POST)
       
    if form.is_valid():
        authenticated_user = authenticate(
            username=form.cleaned_data.get('username', ''),
            password=form.cleaned_data.get('password', ''),
        )
        
        if authenticated_user is not None:
            messages.success(request, 'Your are logged in.')
            login(request, authenticated_user)
        else:
            messages.error(request, 'Invalid credentials')
    else:
        messages.error(request, 'Invalid username or password')
        
    return redirect(reverse('apps.authors:dashboard'))

@login_required(login_url='apps.authors:login', redirect_field_name='next')
def logout_view(request):
    """
    Faz o logout do usuário e redireciona para a página inicial.
    """
    if not request.POST:
        return redirect(reverse('apps.authors:login'))
    
    if request.POST.get('username') != request.user.username:
        return redirect(reverse('apps.authors:login'))
    
    logout(request)
    return redirect(reverse('apps.authors:login'))


@login_required(login_url='apps.authors:login', redirect_field_name='next')
def dashboard(request):
    recipes = Receita.objects.filter(
        is_published=False,
        author=request.user
    )
   
    context = {
        'receitas':recipes
    }
    return render(request, 'authors/pages/dashboard.html',context=context)

@login_required(login_url='apps.authors:login', redirect_field_name='next')
def dashboard_recipe_edit(request,id):
    recipe = Receita.objects.filter(is_published=False,author=request.user,pk=id).first()
    if not recipe:
        raise Http404()
    
    form = AuthorRecipeForm(
        data=request.POST or None,
        files=request.FILES or None,
        instance=recipe 
    )
    context ={
        'receita':recipe,
        'form':form
    }
    if form.is_valid():
        # Agora, o form é válido e eu posso tentar salvar
        recipe = form.save(commit=False)
        recipe.author = request.user
        recipe.preparation_steps_is_html = False
        recipe.is_published = False
        recipe.save()
        messages.success(request, 'Sua receita foi salva com sucesso!')
        return redirect(reverse('apps.authors:dashboard_recipe_edit', args=(id,)))

    return render(
        request,
        'authors/pages/dashboard_recipe.html',
        context=context
    )
    

@login_required(login_url='apps.authors:login', redirect_field_name='next')    
def dashboard_recipe_new(request):
    form = AuthorRecipeForm(data=request.POST or None,files=request.FILES or None,)
    if form.is_valid():
        recipe: Receita = form.save(commit=False)
        recipe.author = request.user
        recipe.preparation_steps_is_html = False
        recipe.is_published = False
        recipe.save()
        messages.success(request, 'Salvo com sucesso!')
        return redirect(reverse('apps.authors:dashboard_recipe_edit', args=(recipe.id,)))
    
    return render(request,'authors/pages/dashboard_recipe.html',
        context={
            'form': form,
            'form_action': reverse('apps.authors:dashboard_recipe_new')
        }
    )

@login_required(login_url='apps.authors:login', redirect_field_name='next')  
def dashboard_recipe_delete(request):
    if not request.POST:
        raise Http404()
    
    POST = request.POST
    id = POST.get('id')
    
    recipe = Receita.objects.filter(
        is_published=False,
        author=request.user,
        pk=id,
    ).first()
    if not recipe:
        raise Http404()
    recipe.delete()
    messages.success(request, 'Deleted successfully.')
    return redirect(reverse('apps.authors:dashboard'))