from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True, blank=True, null=True) 
    telefone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"Nome: {self.nome} - Fone: {self.telefone}"