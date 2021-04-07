# Sniplet
**Free and Open Source Text Replacement Tool based on Python**

**Licensed under GNU GPL 3**

*Version: 1.0.4*

## Description:
Sniplet is a work in progress tool which can do text replacement globally in any of the 3 major desktop OSes 
(Linux, MacOS, Windows). It is a multi-threaded tool which runs quietly in the background with minimal resource 
utilization. It is open source and completely works offline with all the files accessible to the user.

## Features:
1. Custom Text Expansions
2. Multi Threading
3. Background process with low impact
4. Multi Line expansion support
5. Custom config files
6. Easy to install package

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

## Known Issues:
1. Threads crashing if ended abruptly
2. Residual keyboard inputs dumped after aborting (Problem with pynput)
3. Requires X Server on linux (Not available on some distros)



