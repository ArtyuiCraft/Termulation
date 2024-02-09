#imports
import json     #json package needed for settings
import fzfmenus #terminal menu package

from os import listdir           #for game checking
from os.path import isfile, join #for game checking

import os #for running the game and getting location

#config
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
configfile= open(os.path.join(__location__, 'config.json'))  #load the config file
config = json.load(configfile)   #read the config file

console_names = []

for console in config:
    console_names.append(config[console]["name"])

#menu
console = fzfmenus.menu(console_names)
gamepath = config[console]["gamefolder"]
games = [f for f in listdir(gamepath) if isfile(join(gamepath, f))]
game = fzfmenus.menu(games)

#executing the game
os.system(config[console]["command"].replace("%ROM%",f"{gamepath}/{game}"))
