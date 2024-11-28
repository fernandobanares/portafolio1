from django.contrib import admin
from .models import Proyecto

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha', 'categoria', 'herramientas')
    search_fields = ('titulo', 'descripcion', 'categoria')
    list_filter = ('categoria',)