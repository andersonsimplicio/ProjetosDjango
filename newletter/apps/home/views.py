from django.shortcuts import render

def index(request):
    context = {'nome': 'Mundo'}
    return render(request, 'home/index.html', context)
