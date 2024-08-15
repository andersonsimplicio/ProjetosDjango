from rest_framework import viewsets
from .serializers import CategoriaSerializer, IngredienteSerializer
from .models import Categoria, Ingrediente



class CategoriasList(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
      
class IngredienteViewSet(viewsets.ModelViewSet):
    queryset = Ingrediente.objects.all()
    serializer_class = IngredienteSerializer
