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

from ._helper import *
from pynput.keyboard import Key, Controller
import click


class Snipper:
    def __init__(self, filename, verbose):
        self.cfile = filename
        self.verbose = verbose
        map = read_config_file(filename, verbose)
        self.mappings = map
        self.keys = set(map.keys())
        self.buffer = []
        self.curstr = ""

    def replace(self):
        kb = Controller()
        self.curstr = ''.join([str(elem) for elem in self.buffer])
        if self.verbose:
            click.echo(self.curstr)
        if self.curstr in self.keys:
            if self.verbose:
                click.echo("Replacing {} with {}".format(self.curstr, self.mappings[self.curstr]))
            for i in range(len(self.curstr) + 1):
                kb.press(Key.backspace)
                kb.release(Key.backspace)
            for i in range(len(self.mappings[self.curstr])):
                kb.type(self.mappings[self.curstr][i])
            kb.press(Key.backspace)
            kb.release(Key.backspace)
            kb.press(Key.space)
            kb.release(Key.space)
