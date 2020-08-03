from django.contrib import admin
from .models import Receita

# Register your models here.
class ListandoReceitas(admin.ModelAdmin):
    list_display = ('id', 'nome_receita', 'categoria', 'tempo_preparo', 'publicada')
    list_display_links = ('id', 'nome_receita')
    search_fields = ('nome_receita',)
    list_filter = ('categoria',)
    list_per_page = 4
    list_editable = ('publicada',)

admin.site.register(Receita, ListandoReceitas)
