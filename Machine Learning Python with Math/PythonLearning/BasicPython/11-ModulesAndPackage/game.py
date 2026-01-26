# game.py
# import the draw module
# When the import draw directive runs, the Python interpreter looks for a file in the directory in which the script was executed with the module name and a .py suffix. 
# In this case it will look for draw.py. If it is found, it will be imported. 
# If it's not found, it will continue looking for built-in modules.

# You may have noticed that when importing a module, a .pyc file is created. This is a compiled Python file. Python compiles files into Python bytecode so that it won't have to parse the files each time modules are loaded. If a .pyc file exists, it gets loaded instead of the .py file. This process is transparent to the user.
#import draw
from draw import draw_game # can also do from draw import * -> risky # imports all functions from draw module and chance of override

## if not on the same directory, you can use this to look for modules PYTHONPATH=/foo python game.py or sys.path.append("/foo")

## Built in modules https://docs.python.org/3/library/

def play_game():
    ...

def main():
    result = play_game()
    #draw.draw_game(result)
    draw_game()

# this means that if this script is executed, then 
# main() will be executed
if __name__ == '__main__':
    main()


    
## CUSTOM IMPORT NAME

# game.py
# import the draw module
# visual_mode = True
# if visual_mode:
#     # in visual mode, we draw using graphics
#     #import draw_visual as draw
# else:
#     # in textual mode, we print out text
#     #import draw_textual as draw

def main():
    result = play_game()
    # this can either be visual or textual depending on visual_mode
    draw.draw_game(result)

## Python module list.

import urllib
print(dir(urllib))
help(urllib.__cached__)
help(str)