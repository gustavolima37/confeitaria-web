import pandas as pd
from django.core.management.base import BaseCommand
from produtos.models import Produto

class Command(BaseCommand):
    help = "Importa produtos de um arquivo CSV usando pandas"

    def add_arguments(self, parser):
        parser.add_argument("csv_file", type=str)

    def handle(self, *args, **options):
        df = pd.read_csv(options["csv_file"], sep=";")
        df.columns = df.columns.str.strip()

        # Converte preco para número, substitui NaN por 0.0
        df["preco"] = pd.to_numeric(df["preco"], errors="coerce").fillna(0.0)
        df["estoque"] = pd.to_numeric(df["estoque"], errors="coerce").fillna(0)

        print("Colunas encontradas:", df.columns)

        for _, row in df.iterrows():
            Produto.objects.update_or_create(
                nome=row["nome"],
                defaults={
                    "preco": row["preco"],
                    "estoque": row["estoque"],
                },
            )
        self.stdout.write(self.style.SUCCESS("Produtos importados com sucesso!"))