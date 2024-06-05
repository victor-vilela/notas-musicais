from rich import print
from rich.console import Console
from rich.table import Table
from typer import Argument, Typer

from notas_musicais.escalas import escala

console = Console()
app = Typer()


@app.command()
def escalas(
    tonica: str = Argument('c', help='Tônica da Escala'),
    tonalidade: str = Argument('maior', help='Tonalidade da Escala'),
):
    table = Table()

    notas, graus = escala(tonica, tonalidade).values()

    for grau in graus:
        table.add_column(grau)

    table.add_row(*notas)
    console.print(table)
