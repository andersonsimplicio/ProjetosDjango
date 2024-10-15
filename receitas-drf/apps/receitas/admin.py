from django.contrib import admin

from .models import Categoria,Receita


class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Receita)
class RecipeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Categoria, CategoryAdmin)
