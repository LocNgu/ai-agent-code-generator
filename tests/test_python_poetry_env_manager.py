import pytest
from unittest.mock import patch, call
import your_module  # replace with your actual module name


def test_run_command():
    with patch("subprocess.run") as mock_run:
        your_module.run_command("ls")
        mock_run.assert_called_once_with("ls", shell=True, check=True)


def test_create_command():
    assert (
        your_module.create_command("pyenv", "install", "3.8.1") == "pyenv install 3.8.1"
    )
    assert your_module.create_command("remove", "/path/to/dir") == "rm -rf /path/to/dir"


@patch("your_module.run_command")
def test_create_pyenv(mock_run_command):
    your_module.create_pyenv("3.8.1")
    mock_run_command.assert_called_once_with("pyenv install 3.8.1")


@patch("your_module.run_command")
def test_delete_pyenv(mock_run_command):
    your_module.delete_pyenv("3.8.1")
    mock_run_command.assert_called_once_with("pyenv uninstall -f 3.8.1")


@patch("your_module.run_command")
def test_list_pyenv(mock_run_command):
    your_module.list_pyenv()
    mock_run_command.assert_called_once_with("pyenv versions")


@patch("your_module.run_command")
def test_create_poetry(mock_run_command):
    your_module.create_poetry("/path/to/project")
    mock_run_command.assert_called_once_with("poetry new /path/to/project")


@patch("your_module.run_command")
def test_update_poetry(mock_run_command):
    your_module.update_poetry("/path/to/project")
    mock_run_command.assert_called_once_with("poetry cd /path/to/project && update")


@patch("your_module.run_command")
def test_delete_poetry(mock_run_command):
    your_module.delete_poetry("/path/to/project")
    mock_run_command.assert_called_once_with("rm -rf /path/to/project")
