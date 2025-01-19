from django.http import Http404
from django.shortcuts import redirect, render

from apps.authors.forms import RegisterForms

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
    }
    
    return render(request, 'authors/pages/register_view.html',context=context)

def register_create(request):   
    
    if not request.POST:
        raise Http404()
    POST = request.POST
    request.session['register_form_data'] = POST
    form = RegisterForms(request.POST)  
    
    context = {
        'form':form,
    }
    
    return redirect('apps.authors:register') 