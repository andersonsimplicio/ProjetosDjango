from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
# Create your views here.
from django.views.generic import TemplateView
from apps.siga.form import LoginForm
from apps.siga.models import PerfilUsuario

class HomeView(TemplateView):
    template_name = "siga/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = LoginForm()  # adiciona o form ao contexto
        return context
    
        
        return render(request, 'siga/home.html', {'form': form})
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)

                # Busca o perfil vinculado ao usuário
                try:
                    perfil = PerfilUsuario.objects.get(user=user)
                except PerfilUsuario.DoesNotExist:
                    print('nao existe!')
                    return redirect('siga:home') 

                # Redireciona conforme o tipo
                if perfil.tipo == 'aluno':
                    return redirect('alunos:dashboard')
                elif perfil.tipo == 'professor':
                    return redirect('professores:dashboard')
                elif perfil.tipo == 'admin':
                    return redirect('admin:index')  # ou uma view personalizada
            else:
                form.add_error(None, "Usuário ou senha inválidos.")
                #messages.error(request, 'Usuário ou senha inválidos.')
    else:
        form = LoginForm()
    
    return render(request, 'siga/home.html', {'form': form})
    