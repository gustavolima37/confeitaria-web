# pedidos/management/commands/importar_pedidos.py
import pandas as pd
from django.core.management.base import BaseCommand
from pedidos.models import Pedido
from clientes.models import Cliente
from produtos.models import Produto

class Command(BaseCommand):
    help = "Importa pedidos de um arquivo CSV usando pandas"

    def add_arguments(self, parser):
        parser.add_argument("csv_file", type=str)

    def handle(self, *args, **options):
        df = pd.read_csv(options["csv_file"])

        for _, row in df.iterrows():
            try:
                cliente = Cliente.objects.get(cpf=row["cpf_cliente"])
                produto = Produto.objects.get(nome=row["produto"])  # busca o objeto Produto

                Pedido.objects.update_or_create(
                    cliente=cliente,
                    produto=produto,
                    data_pedido=row["data_pedido"],
                    defaults={
                        "quantidade": int(row["quantidade"]),
                        "forma_pagamento": row["forma_pagamento"],
                        "data_entrega": row["data_entrega"],
                    },
                )
            except Cliente.DoesNotExist:
                self.stdout.write(self.style.WARNING(f"Cliente com CPF {row['cpf_cliente']} não encontrado."))
            except Produto.DoesNotExist:
                self.stdout.write(self.style.WARNING(f"Produto '{row['produto']}' não encontrado."))

        self.stdout.write(self.style.SUCCESS("Pedidos importados com sucesso!"))