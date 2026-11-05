# Project-LANCER
A voice-controlled (not generative) AI that runs on the user's PC!

Can be used with Modrinth, Discord, Google Chrome and Steam.

## Setup Guide
- Open a PowerShell window in the folder with Shift + Right Click
- Run
```powershell
pip install -r requirements.txt
```

### FOR STEAM
- Create a Steam Web API Key [here](https://steamcommunity.com/dev/apikey)
- Open config.json in your preferred text editor
- Paste in your Web API Key.
- Paste in your 64-bit Steam ID (DO NOT PASTE IN A CUSTOM URL!!!)
- Save the file and exit

You can now use all of LANCER's functions! Enjoy!

LANCER does not send information outside of your PC. I will not know any information LANCER receives from your PC.

Information for activating on startup will be below.

## Key Commands
- help/listcommands - Opens Notepad and lists every command to the user
- open/run - Runs an application in AppData/Roaming/Microsoft/Windows/Start Menu/Programs. Note that it doesn't check folders, so Steam shortcuts should be moved to this folder instead of the Steam subfolder.
- close/kill - Closes an application.
- focus - Focuses on the window you choose
- fullscreen - Makes the selected app fullscreen.
- switch window (left/right) - Switches the monitor the application is on.

## Activating on Startup
- Press Win + R
- Type
```
shell:startup
```
- Create a new text file and name it whatever you want
- Open it in the text editor of your choice
- Type in
```
Dim WinScriptHost
Set WinScriptHost = CreateObject("WScript.Shell")
WinScriptHost.Run Chr(34) & "<path to LANCER>" & Chr(34), 0
Set WinScriptHost = Nothing
```
- Save the file and exit it.
- Change the extension of the file to .vbs

LANCER should now run on startup.

## Forks
Forks of this project are permitted, so long as they are private and are for personal use. Failure to comply will result in a DMCA.

## Disclaimers
As mentioned before, LANCER will not send any information outside your PC. However, certain behaviours, such as refreshing the Web API for Steam, may give the illusion that they steal info. You are welcome to look through the code yourself if you wish to make sure.

To use Steam commands, you must be logged into Steam on a browser.

This project is only for Windows PCs. Some functions may not work on Apple or Linux-based devices.

No generative AI has been used when making this project. LANCER himself is also not a generative AI.
