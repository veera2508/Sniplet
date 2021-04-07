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
    """
    Class which holds the data and functions required for snipper

        Attributes:
            current_input (list): Stores the input till space is pressed
            lis (bool): Flag to control listening
            running (bool): Flag to control running of the program
            kb (Keyboard.controller): Controller used to create keyboard actions
            listener (Keyboard.listener): Listens to the keyboard
            verbose (bool): Printing verbose outputs
            mappings (dict): Holds the mapping of Text Replacements to their Shortcuts
    """

    def __init__(self, filename, verbose):
        self.current_input = []
        self.lis = False
        self.running = False
        self.kb = Controller()
        self.listener = 0
        self.verbose = verbose
        self.mappings = read_config_file(filename, verbose)

    def on_press(self, key):
        """
        Text replacement is done. Called on press of a key
            Args:
                key (Keys.key): Key being pressed
            Returns:
                bool: Stop or continue listening
        """
        keys = set(self.mappings.keys())
        try:
            self.current_input.append(key.char)
        except AttributeError:
            self.listener.stop()
            self.running = False
            if key == Key.space:
                curstr = ''.join([str(elem) for elem in self.current_input])
                if self.verbose:
                    print(curstr)
                if curstr in keys:
                    if self.verbose:
                        click.echo("Replacing {} with {}".format(curstr, self.mappings[curstr]))
                    for i in range(len(curstr) + 1):
                        self.kb.press(Key.backspace)
                        self.kb.release(key.backspace)
                    for i in range(len(self.mappings[curstr])):
                        self.kb.type(self.mappings[curstr][i])
                    self.kb.press(Key.backspace)
                    self.kb.release(key.backspace)
                    self.kb.press(Key.space)
                    self.kb.release(key.space)
                    self.current_input = []
                self.current_input = []
            elif key == Key.backspace and self.current_input:
                self.current_input.pop()

    def on_release(self, key):
        """
            Called on release of a key (Not working properly)
                Args:
                    key (Keys.key): Key being pressed
                Returns:
                    bool: Stop or continue listening
        """
        if key == Key.esc:
            self.lis = False
            self.running = False
            self.listener.stop()
            return False

    def run(self):
        """Starts the listening process"""
        self.lis = True
        self.running = False
        self.listener = keyboard.Listener(on_press=lambda event: self.on_press(event),
                                          on_release=lambda event: self.on_release(event))  # Creating a listener
        while self.lis: # Main Loop
            if not self.running:
                self.listener.stop()
                self.listener = keyboard.Listener(on_press=lambda event: self.on_press(event),
                                                  on_release=lambda event: self.on_release(event)) # Start new listener
                self.running = True
                self.listener.start() # Starting the thread
                self.listener.join() # Joining the threads in a blocking way
