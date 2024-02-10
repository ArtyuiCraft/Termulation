# Termulation
Termulation is a terminal base retro game launcher it uses fzf for selecting the system and game
# Install
make sure you have fzf installed

for windows:
download the exe

for linux and mac:
download the python file and then chmod it to make it executable and then just run it
# config
## !!!THE CONFIG FILE CAN'T BE EMPTY ELSE IT WILL CRASH!!!

the  config file is expected next to the executable. it has to be named config.json
## Adding a system
adding a system is easy you just copy this example config and add in the parameters
```json
{
	"name of console": {
		"name": "name of console"
		"gamefolder": "full path to the folder  with roms"
		"command": "emulator -f %ROM%"
	}
}
```
the `%ROM%` gets replaced with the path  of the rom
