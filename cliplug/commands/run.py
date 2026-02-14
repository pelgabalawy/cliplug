import click
import subprocess

from cliplug.storage.yaml_store import load_data


@click.command()
@click.option(
    '--command',
    "-c",
    required=True,
    help="Run one of the saved command or a new command"
)
def run(command):
    data = load_data()
    if command in data["commands"]:
        cmd_to_run = data["commands"][command]
        result = subprocess.run(
                    cmd_to_run.split(" "),
                    capture_output=True,
                    text=True,
                    check=True,
                    shell=True
                )
        click.echo(result.stdout)
    else:
        click.secho("command not found. If you want to see the available commands please use the cliplug list", fg="red")