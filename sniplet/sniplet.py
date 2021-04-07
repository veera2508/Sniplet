"""
    This file is part of Sniplet.

    Sniplet is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Sniplet is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Sniplet.  If not, see <https://www.gnu.org/licenses/>.
    """
import click
from ._snipper import *

__version__ = "1.0.5"

@click.command()
@click.option('--verbose', is_flag=True, help="Print Verbose Messages")
@click.option('--config', is_flag=True, help="Configure the Snippets")
@click.option('--version', is_flag=True, help="Get the version number")
@click.option('--start', required="false", default="", help="Start the snipper with given config file as filename ("
                                                            "Follow file "
                                                            "convention in --help)")
def main(verbose, config, version, start):
    """
    Sniplet

    A lightweight, threaded, multiplatform text replacement tool which works on Windows, MacOS and Linux

    Note: Requires keyboard access on MacOS and X Server on Linux (for pynput)

    To configure replacement file within the terminal use --config. To use your own config file please mention it
    with --start (Path Required) and follow the given specification

    File Specification:

    Short:

    [Shortcut]

    Repl:

    [Replacement]

    A Sample Specification is provided with sample_config.txt inside config-files

    !!Turn off the listener from the terminal using the keyboard interrupt to avoid unnecessary leakage of text!!

    Author: Veeraraghavan Narasimhan

    Email: virunarasimhan25@gmail.com

    Licensed under GNU General Public License 3
    """

    click.echo("Licensed under GNU General Public License 3\n")

    if start != "":
        snip = Snipper(start, verbose)
        snip.run()

    elif config:
        create_config_file()

    elif version:
        click.echo(__version__)

    elif start == "":
        click.echo("Enter the filename you created using config: ")
        filename = input()
        filename = "./config-files/"+filename
        snip = Snipper(filename, verbose)
        snip.run()







