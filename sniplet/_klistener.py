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

from pynput import keyboard
from ._snipper import *
from ._mathsolver import MathSolver
from pynput.keyboard import Key, Controller


class KListener:
    """
    Class which holds the data and functions required for keyboard listener

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
        self.lis = False
        self.running = False
        self.listener = 0
        self.verbose = verbose
        self.snipper = Snipper(filename, verbose)
        self.mathsolver = MathSolver(verbose)
        self.buffer = []
        self.current = set()
        self.kb = Controller()

    def on_press(self, key):
        """
        Text replacement is done. Called on press of a key
            Args:
                key (Keys.key): Key being pressed
            Returns:
                bool: Stop or continue listening
        """
        try:
            self.buffer.append(key.char)
        except AttributeError:
            self.listener.stop()
            self.running = False
            if key == Key.space and self.buffer:
                result, flag = self.processbuffer()
                if result:
                    for i in range(len(self.buffer) + 1):
                        self.kb.press(Key.backspace)
                        self.kb.release(Key.backspace)
                    for i in range(len(result)):
                        self.kb.type(result[i])
                    if flag:
                        self.kb.press(Key.backspace)
                        self.kb.release(Key.backspace)
                    self.kb.press(Key.space)
                    self.kb.release(Key.space)
                self.buffer = []
            elif key == Key.backspace and self.buffer:
                self.buffer.pop()

    def on_release(self, key):
        """
            Called on release of a key (Not working properly on MacOs)
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
        while self.lis:  # Main Loop
            if not self.running:
                self.listener.stop()
                self.listener = keyboard.Listener(on_press=lambda event: self.on_press(event),
                                                  on_release=lambda event: self.on_release(event))  # Start new listener
                self.running = True
                self.listener.start()  # Starting the thread
                self.listener.join()  # Joining the threads in a blocking way

    def processbuffer(self):
        if self.buffer[0] == "=" and self.buffer[-1] == "=":
            return ["0"], 0
        else:
            return self.snipper.replace(self.buffer), 1
