import click
from cliplug.storage.yaml_store import load_data, delete_command


@click.command()
@click.option('--reference', "-r", required=True, help="the reference to the command that will be deleted")
def delete(reference):
    data = load_data()
    if reference in data["commands"]:
        command = data["commands"][reference]
        delete_command(reference)
        click.secho(f"The following command has been deleted: {reference}: {command}", fg="green")
    else:
        click.secho("Command doesn't exist!", fg="red")