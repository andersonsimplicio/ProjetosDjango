from django.urls import path,include
from .views import CategoriasList, IngredienteViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'categorias', CategoriasList)
router.register(r'ingredientes', IngredienteViewSet)

urlpatterns = [
   path('', include(router.urls)),
]
