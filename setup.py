"""Setup.py: Setup tools control

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

import re
from setuptools import setup

version = re.search('^__version__\s*=\s*"(.*)"', open('sniplet/sniplet.py').read(), re.M).group(1)
setup(
    name="sniplet",
    packages=["sniplet"],
    entry_points={
        "console_scripts": ['sniplet = sniplet.sniplet:main']
    },
    version=version,
    description="Python command line application for text replacement",
    author="Veeraraghavan-Narasimhan",
    author_email="virunarasimhan25@gmail.com",
    url="https://github.com/veera2508",
    install_requires=["pynput", "click"]
)
