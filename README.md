<div align = "center">

<img src="./images/logo.png" width="100" height="100"></img>

</div>

<h1 align = "center">Sniplet</h1>

<p align = "center">Free and Open Source Text Replacement Tool based on Python</p>


<div align = "center">

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg)](http://perso.crans.org/besson/LICENSE.html)
[![Open Source Love svg2](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)]()
[![Version](https://img.shields.io/github/v/release/veera2508/sniplet)]()
[![Stars](https://img.shields.io/github/stars/veera2508/sniplet?style=social)]()

</div>


## Description:
Sniplet is a work in progress tool which can do text replacement globally in any of the 3 major desktop OSes 
(Linux, MacOS, Windows). It is a multi-threaded tool which runs quietly in the background with minimal resource 
utilization. It is open source and completely works offline with all the files accessible to the user.

## Features:
1. Custom Text Expansions
2. Background process with low resource utilization
3. Multi Line expansion support
4. Custom config files

## Installation:
**Python is required**

**Might require admin or su permission to install**

**Add sniplet to the PATH variable**

### Installing using pip:
      pip install sniplet==1.0.4
### Installing from source:
1. Download the files from github
2. Run the following command in the terminal

        python setup.py install
3. If you don't want Sniplet to be installed globally, it is recommended to create a virtualenv to install it

## Configuration:
1. Run the following command to configure the text replacements
        
        sniplet --config
2. Alternatively, you can create your own file with the following specification and save it as a txt file:

        Short:
        [shortcut name]
        Repl:
        [Replacement lines]
        ...

## Usage:
1. Start Sniplet by using the following command. Replace filepath by the path to your custom file or leave it blank for 
it to choose the one you created using --config
   
        sniplet --start [FILEPATH]
2. To stop Sniplet use the keyboard interrupt in the terminal

## Help
Use the following command to get more info about usage and configuration
      
      sniplet --help

## Known Issues:
1. Threads crashing if ended abruptly
2. Residual keyboard inputs dumped after aborting (Problem with MacOS)



