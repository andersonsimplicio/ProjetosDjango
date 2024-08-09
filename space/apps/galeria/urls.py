from django.urls import path
from .views import index, imagem,buscar,nova_image,editar_image,deletar_image

urlpatterns = [
    path('', index, name='home'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path('buscar/', buscar, name='buscar'),
    path('new-image/', nova_image, name='nova-imagem'),
    path('delete-image/', deletar_image, name='delete-imagem'),
    path('editar-image/', editar_image, name='editar-imagem'),
]