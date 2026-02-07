from django.db import models
from clientes.models import Cliente



# Create your models here.

class Endereco(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='enderecos')
    rua = models.CharField(max_length= 100 )
    numero = models.CharField(max_length=10)
    bairro = models.CharField (max_length=50)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    cep = models.CharField(max_length= 10)

    def __str__(self):
            return f"{self.rua},{self.numero}"


