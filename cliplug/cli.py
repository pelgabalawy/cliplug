import click
from cliplug.commands.list import list_commands
from cliplug.commands.run import run

@click.group()
def main():
    """Cliplug - A CLI plugin system"""
    pass

main.add_command(list_commands, name="list")
main.add_command(run, name="run")

if __name__ == "__main__":
    main()
