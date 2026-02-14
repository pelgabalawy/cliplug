import click
from cliplug.storage.yaml_store import add_command, load_data


@click.command()
@click.option('--command', "-c", required=True, help="add/save a new command")
@click.option('--reference', "-r", required=True, help="the added command reference")
def add(command, reference):
    data = load_data()
    if reference not in data["commands"]:
        add_command(reference, command)
        click.secho(f"The following command has been added: {reference}: {command}", fg="green")
    else:
        click.secho("Command already exists!", fg="red")