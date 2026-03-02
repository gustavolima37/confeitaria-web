from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    disponibilidade = models.BooleanField(default=True)
    estoque = models.PositiveIntegerField(default=0)  # único campo de quantidade

    def __str__(self):
        return f'{self.nome} - R$ {self.preco} (Estoque: {self.estoque})'

    def save(self, *args, **kwargs):
        # Atualiza disponibilidade automaticamente
        self.disponibilidade = self.estoque > 0
        super().save(*args, **kwargs)

    def reduzir_estoque(self, quantidade):
        self.estoque = max(self.estoque - quantidade, 0)
        self.save()