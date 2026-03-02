from django.db import models
from clientes.models import Cliente


# Create your models here.

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='pedidos')
    cpf_cliente = models.CharField(max_length= 11)
    produto = models.CharField(max_length= 50)
    quantidade = models.PositiveIntegerField(default=0)
    valor_encomenda = models.DecimalField(max_digits=8, decimal_places=2)
    forma_pagamento = models.CharField(max_length= 30)
    data_pedido = models.DateTimeField()
    data_entrega = models.DateField()

def __str__(self):
        return f'CPF: {self.cpf_cliente}'

