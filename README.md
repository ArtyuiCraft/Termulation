# Termulation
Termulation is a terminal-based retro game launcher. It uses fzf for selecting the system and game.

## Install
Make sure you have fzf installed.

### Automatic Installation
Not yet implemented; will be available in version 1.1.

### Manual Installation
#### Windows:
Download the .exe and add it to the PATH so that you can run it from anywhere.

#### Linux and macOS:
Download the binary, then chmod it to make it executable, and finally, run it.

## Configuration
### !!!THE CONFIG FILE CAN'T BE EMPTY, OTHERWISE IT WILL CRASH!!!

The config file is expected to be located next to the executable and must be named `config.json`.

### Adding a System
Adding a system is easy; you just need to copy this example config and fill in the parameters:

```json
{
	"name of console": {
		"name": "name of console",
		"gamefolder": "full path to the folder with ROMs",
		"command": "emulator -f %ROM%"
	}
}
```
The `%ROM%` placeholder gets replaced with the path of the ROM.
