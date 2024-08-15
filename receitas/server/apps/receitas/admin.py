from django.contrib import admin
from .models import Categoria, Ingrediente



@admin.register(Categoria)
class CategoriasAdmin(admin.ModelAdmin):
    list_display = ('nome', 'get_imagem_preview')
    search_fields = ('nome',)
    filter_horizontal = ('ingredientes',)  # Permite selecionar múltiplos ingredientes de forma fácil
    list_filter = ('ingredientes',)  # Adiciona um filtro por ingredientes na lista de receitas

    def get_imagem_preview(self, obj):
        if obj.imagem:
            return f'<img src="{obj.imagem.url}" width="100" height="100" />'
        return 'No Image'
    
    get_imagem_preview.allow_tags = True
    get_imagem_preview.short_description = 'Image Preview'    
   

@admin.register(Ingrediente)
class IngredienteAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)