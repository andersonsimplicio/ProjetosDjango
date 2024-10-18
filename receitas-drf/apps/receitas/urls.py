from django.urls import path
from .views import home,receita,categoria

app_name = 'apps.receitas'

urlpatterns = [
    path('',home,name='home'),
    path('receita/<int:id>/',receita,name='receita'),
    path('receitas/categoria/<int:category_id>/',categoria, name="categoria"),
]
