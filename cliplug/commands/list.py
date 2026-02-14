import click
from cliplug.storage.yaml_store import load_data

@click.command()
def list_commands():
    data = load_data()
    click.secho("----------------\nlist of commands:\n----------------")
    for ref, com in data["commands"].items():
        click.secho(f"\t{ref}: {com}", fg="green")

