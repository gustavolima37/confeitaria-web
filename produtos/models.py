from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    disponibilidade = models.BooleanField(default=True)
    quantidade = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f'Nome: {self.nome} - Preço: {self.preco} - Qtd: < {self.quantidade} >'