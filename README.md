# Termulation
Termulation is a terminal base retro game launcher it uses fzf for selecting the system and game
# Install
download the program and make sure that you have fzf installed
# config
the  config file is expected next to the executable called config.json
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
