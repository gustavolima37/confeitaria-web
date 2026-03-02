from django.db import models
from clientes.models import Cliente
from produtos.models import Produto


# Create your models here.

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='pedidos')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='pedidos')
    quantidade = models.PositiveIntegerField(default=1)
    forma_pagamento = models.CharField(max_length=30)
    data_pedido = models.DateTimeField(auto_now_add=True)
    data_entrega = models.DateField()

    @property
    def valor_encomenda(self):
        return self.produto.preco * self.quantidade

    def save(self, *args, **kwargs):
        # Se for um pedido novo (sem ID ainda), reduz estoque
        if not self.pk:
            self.produto.reduzir_estoque(self.quantidade)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Pedido #{self.id} - Cliente: {self.cliente.nome}'


