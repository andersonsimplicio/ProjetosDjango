from rest_framework import serializers
from .models import Categoria, Ingrediente


class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = ['nome']
   

class CategoriaSerializer(serializers.ModelSerializer):
    ingredientes = IngredienteSerializer(many=True)  # Inclui uma lista de ingredientes

    class Meta:
        model = Categoria
        fields = ['nome', 'ingredientes', 'imagem']