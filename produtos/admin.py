from django.contrib import admin
from .models import Produto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("nome", "preco", "estoque", "disponibilidade")
    list_editable = ("estoque", "preco")  # campos que podem ser editados direto na lista
    search_fields = ("nome",)
    list_filter = ("disponibilidade",)