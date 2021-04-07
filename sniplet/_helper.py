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
import os


def read_config_file(filename, verbose):
    """
    Reads the given config file and produces an error if format is wrong

    Args:
        filename(str): File name of file to be opened
        verbose(bool): Control verbose output

    Returns:
        mappings (dict): Holds the mapping of Text Replacements to their Shortcuts
    """

    try:
        f = open(filename, "r")
        lines = f.readlines()
        mappings = {}
        i = 0
        while i < len(lines):
            maplist = []
            if lines[i] == "Short:\n":
                i += 1
                short = lines[i].rstrip("\n")
                i += 1
            else:  # No short tag
                click.echo("Wrong file format!, Aborting....")
                exit(1)
            if lines[i] == "Repl:\n":
                i += 1
                while i < len(lines) and lines[i] != "Short:\n":
                    maplist.append(lines[i])
                    i += 1
                i -= 1
            else:  # No repl tag
                click.echo("Wrong file format!, Aborting....")
                exit(1)

            mappings[short] = maplist  # Add the corresponding lines to the mapping
            i += 1

        if verbose:
            click.echo("Found {} entries in file\n".format(len(mappings)))
            for j in mappings.keys():
                click.echo("Short: {}\n".format(j))
                click.echo("Repl: \n")
                for k in mappings[j]:
                    click.echo(k)
        return mappings
    except FileNotFoundError:   # Exception raised if file not found
        click.echo("The specified file was not found!, Aborting....")
        exit(1)


def create_config_file():
    """
    Creates a config file from given user input and produces an error if format is wrong
    """

    click.echo("Enter the file name: ")
    filename = input()
    mappings = {}

    while True:
        click.echo("\n1.Add new replacement\n2.Delete replacement\n3.Show all replacements\n4.Exit\n")
        choice = input()
        if choice == "1":
            click.echo("Enter the shortcut: ")
            short = input()
            click.echo("Enter the Replacement: ")
            repl = input()
            mappings[short] = repl

        elif choice == "2":
            click.echo("Enter the shortcut for the replacement to be deleted: ")
            short = input()
            try:
                del mappings[short]
            except KeyError:
                click.echo("Record not found\n")

        elif choice == "3":
            for i in mappings.keys():
                click.echo("\nShortcut: {} -> Replacement: {}".format(i, mappings[i]))

        elif choice == "4":
            break

        else:
            click.echo("Please choose the correct option!\n")

    click.echo("Writing to file {} .....".format(filename))

    try:
        os.mkdir("./config-files/")
    except FileExistsError:
        pass

    f = open("./config-files/"+filename, "w")
    for i in mappings.keys():
        f.write("Short:\n")
        f.write(i + "\n")
        f.write("Repl:\n")
        f.write(mappings[i] + "\n")
    click.echo("File created successfully!")
