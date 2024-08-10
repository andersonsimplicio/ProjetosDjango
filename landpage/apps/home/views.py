from django.shortcuts import render

def index(request):
    context = {'nome': 'Mundo'}
    return render(request, 'index.html', context)
