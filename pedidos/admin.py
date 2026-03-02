from django.contrib import admin
from .models import Pedido

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ("cliente", "produto", "quantidade", "valor_encomenda", "data_pedido", "data_entrega", "forma_pagamento")
    list_filter = ("forma_pagamento", "data_pedido")
    search_fields = ("cliente__nome", "produto__nome")
    ordering = ("-data_pedido",)

    # Exibir valor calculado no admin
    def valor_encomenda(self, obj):
        return obj.valor_encomenda
    valor_encomenda.short_description = "Valor Total"