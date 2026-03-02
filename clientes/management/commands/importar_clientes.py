# clientes/management/commands/importar_clientes.py
import pandas as pd
from django.core.management.base import BaseCommand
from clientes.models import Cliente
from enderecos.models import Endereco

class Command(BaseCommand):
    help = "Importa clientes e endereços de um CSV usando pandas"

    def add_arguments(self, parser):
        parser.add_argument("csv_file", type=str)

    def handle(self, *args, **options):
        df = pd.read_csv(options["csv_file"])

        for _, row in df.iterrows():
            cliente, _ = Cliente.objects.update_or_create(
                cpf=row["cpf"],
                defaults={
                    "nome": row["nome"],
                    "telefone": row["telefone"],
                    "email": row["email"],
                },
            )
            Endereco.objects.update_or_create(
                cliente=cliente,
                rua=row["rua"],
                numero=row["numero"],
                defaults={
                    "bairro": row["bairro"],
                    "complemento": row.get("complemento", ""),
                    "cidade": row.get("cidade", ""),
                    "estado": row.get("estado", ""),
                    "cep": row["cep"],
                },
            )
        self.stdout.write(self.style.SUCCESS("Clientes e endereços importados com sucesso!"))