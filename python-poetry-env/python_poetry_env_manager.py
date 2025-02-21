import subprocess
import click

# Constants for the commands
COMMANDS = {"pyenv": "pyenv", "poetry": "poetry", "remove": "rm -rf"}


def run_command(command):
    """Run a command using subprocess."""
    subprocess.run(command, shell=True, check=True)


def create_command(command_key, action, argument=None):
    """Create a command string."""
    command = COMMANDS[command_key]
    if argument:
        return f"{command} {action} {argument}"
    return f"{command} {action}"


@click.group()
def cli():
    pass


@cli.command()
@click.argument("version")
def create_pyenv(version):
    """Create a new pyenv environment."""
    run_command(create_command("pyenv", "install", version))


@cli.command()
@click.argument("version")
def delete_pyenv(version):
    """Delete a pyenv environment."""
    run_command(create_command("pyenv", "uninstall -f", version))


@cli.command()
def list_pyenv():
    """List all pyenv environments."""
    run_command(create_command("pyenv", "versions"))


@cli.command()
@click.argument("path")
def create_poetry(path):
    """Create a new Poetry project."""
    run_command(create_command("poetry", "new", path))


@cli.command()
@click.argument("path")
def update_poetry(path):
    """Update a Poetry project."""
    run_command(create_command("poetry", f"cd {path} && update"))


@cli.command()
@click.argument("path")
def delete_poetry(path):
    """Delete a Poetry project."""
    run_command(create_command("remove", path))


if __name__ == "__main__":
    cli()
