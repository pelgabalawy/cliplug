import click
from cliplug.commands.list import list_commands
from cliplug.commands.remove import delete
from cliplug.commands.run import run
from cliplug.commands.add import add

@click.group()
def main():
    """Cliplug - A CLI plugin system"""
    pass

main.add_command(list_commands, name="list")
main.add_command(run, name="run")
main.add_command(add, name="add")
main.add_command(delete, name="delete")

if __name__ == "__main__":
    main()
