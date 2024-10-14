from django.urls import path
from .views import home,receita

app_name = 'receitas'

urlpatterns = [
    path('',home,name='home'),
    path('receita/<int:id>/',receita,name='receita'),
]
