import click
import subprocess

#TODO: the following is for testing only
from cliplug.commands.list import COMMAND_REGISTRY


@click.command()
@click.option(
    '--command',
    "-c",
    required=True,
    help="Run one of the saved command or a new command"
)
def run(command):
    if command in COMMAND_REGISTRY:
        cmd_to_run = COMMAND_REGISTRY[command]
        result = subprocess.run(
                    cmd_to_run.split(" "),
                    capture_output=True,
                    text=True,
                    check=True,
                    shell=True
                )
        click.echo(result.stdout)
    else:
        click.echo("command not found. If you want to see the available commands please use the cliplug list")