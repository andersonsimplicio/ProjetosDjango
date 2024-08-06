from django.urls import path
from .views import index, imagem

urlpatterns = [
    path('', index, name='home'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
]