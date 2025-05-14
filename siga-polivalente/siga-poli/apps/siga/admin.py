from django.contrib import admin

from django.contrib import admin
from .models import PerfilUsuario

@admin.register(PerfilUsuario)
class PerfilUsuarioAdmin(admin.ModelAdmin):
    list_display = ['user','tipo']
    list_filter = ['tipo']
    search_fields = ['user__username', 'user__email']


