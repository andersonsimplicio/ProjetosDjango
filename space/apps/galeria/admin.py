from django.contrib import admin

from apps.galeria.models import Fotografia

class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id","nome","legenda","foto","publicada","date")
    list_display_links = ("id","nome","foto")
    search_fields = ("nome",)
    list_filter = ("categoria",)
    list_per_page = 10
    list_editable = ("publicada",)


admin.site.register(Fotografia,ListandoFotografias)