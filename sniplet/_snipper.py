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
from pynput import keyboard
from pynput.keyboard import Key, Controller
import click

class Snipper:
    def __init__(self, filename, verbose):
        self.cfile = filename
        self.verbose = verbose
        map = read_config_file(filename, verbose)
        self.mapping = map
        self.kb = Controller()
        self.keys = set(map.keys())
        self.current_input = []
        self.curstr = ""

    def replace(self):
        self.curstr = ''.join([str(elem) for elem in self.current_input])
        if self.verbose:
            print(self.curstr)
        if self.curstr in self.keys:
            if self.verbose:
                click.echo("Replacing {} with {}".format(self.curstr, self.mappings[curstr]))
            for i in range(len(self.curstr) + 1):
                self.kb.press(Key.backspace)
                self.kb.release(Key.backspace)
            for i in range(len(self.mappings[self.curstr])):
                self.kb.type(self.mappings[self.curstr][i])
            self.kb.press(Key.backspace)
            self.kb.release(Key.backspace)
            self.kb.press(Key.space)
            self.kb.release(Key.space)
            self.current_input = []
        self.current_input = []
