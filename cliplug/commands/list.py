import click
from cliplug.storage.yaml_store import load_data

@click.command()
@click.option(
    '--keywords',
    "-k",
    required=False,
    multiple=True,
    default=None,
    help="[Optional] filter command by keywords (-k foo -k bar for muli keywords)"
)
def list_cmd(keywords):
    data = load_data()
    if data["commands"]:
        click.secho("----------------\nlist of commands:\n----------------")
        for ref, com in data["commands"].items():
            if keywords:
                if any([keyword in ref or keyword in com for keyword in keywords]):
                    click.secho(f"\t{ref}: {com}", fg="green")
            else:
                click.secho(f"\t{ref}: {com}", fg="green")
    else:
        click.secho("No commands found!", fg="red")

