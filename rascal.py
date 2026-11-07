"""
Project: LANCER
Gale2222
"""
### --- IMPORTS --- ###
import os
import json
import psutil
import win32api, win32con
import pygetwindow as gw
import pyscreenshot
import time
import speech_recognition as sr
import pyttsx3
import random
import pathlib
from pocketsphinx import LiveSpeech
from pyautogui import press, typewrite, hotkey, keyDown, keyUp

from steamfunctions import get_games, get_review_score_last, get_description_last

### --- VARIABLES --- ###
dictation = False
respond = False
shutDownPath = "shutdown.bat"
r = sr.Recognizer()
r.dynamic_energy_threshold = True
ttsengine = pyttsx3.init()
voices = ttsengine.getProperty("voices")
ttsengine.setProperty("voice", voices[0].id)

runPath = str(pathlib.Path.home() / "AppData/Roaming/Microsoft/Windows/Start Menu/Programs/")
runList = list(runPath)
for i in range(len(runList)):
    if runList[i] == "\\":
        runList[i] = "/"
runList.append("/")
runPath = ''.join(runList)

try:
    f = open("steamgames.txt")
    fileList = f.read()
    steamList = fileList.splitlines()
    f.close()
except:
    f = open("steamgames.txt", "w")
    steamList = []
    f.close()

try:
    f = open("steamappids.txt")
    fileList = f.read()
    steamAppIdList = fileList.splitlines()
    f.close()
except:
    f = open("steamappids.txt", "w")
    steamAppIdList = []
    f.close()

with open("config.json") as config_file:
    config = json.load(config_file)
    browser = config["browser"]

### --- FUNCTIONS --- ###

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def checkForShorthands(text):
    if text == ("Mod") or text == ("mod") or text == "modern" or text == "Modern":
        return "ModrinthApp"
    if text == "Del":
        return "Deltarune"
    else:
        return text

# ----- SYSTEM FUNCTIONS ----- #

def runProgram(text):
    text = checkForShorthands(text)
    try:
        os.startfile(f"{runPath}{text}.lnk")
        ttsengine.say(f"running {text}", "Running program")
        ttsengine.runAndWait()
    except FileNotFoundError:
        try:
            os.startfile(f"{runPath}{text}.url")
            ttsengine.say(f"running {text}", "Running program")
            ttsengine.runAndWait()
        except FileNotFoundError:
            text.upper()
            try:
                os.startfile(f"{runPath}{text}.lnk")
                ttsengine.say(f"running {text}", "Running program")
                ttsengine.runAndWait()
            except:
                try:
                    os.startfile(f"{runPath}{text}.url")
                    ttsengine.say(f"running {text}", "Running program")
                    ttsengine.runAndWait()
                except FileNotFoundError:
                    text.title()
                    try:
                        os.startfile(f"{runPath}{text}.lnk")
                        ttsengine.say(f"running {text}", "Running program")
                        ttsengine.runAndWait()
                    except:
                        try:
                            os.startfile(f"{runPath}{text}.url")
                            ttsengine.say(f"running {text}", "Running program")
                            ttsengine.runAndWait()
                        except:
                            print(f"There is no program named {text.title()}")
                            ttsengine.say(f"{text} does not exist", "Running program")
                            ttsengine.runAndWait()

def killProgram(text):
    text = checkForShorthands(text)
    programKill = f"{text}.exe"
    for p in psutil.process_iter():
        if p.name() == programKill:
            p.kill()
    programKill = f"{text.upper()}.exe"
    for p in psutil.process_iter():
        if p.name() == programKill:
            p.kill()

def takeAScreenshot():
    image = pyscreenshot.grab()
    ts = time.time()
    image.save(f"screenshots/{ts}.png")

def windowSwitchLeft():
    hotkey("win", "shift", "left")

def windowSwitchRight():
    hotkey("win", "shift", "right")

def fullscreen():
    press("f11")

def focus(text):
    text = checkForShorthands(text)
    try:
        win = gw.getWindowsWithTitle(f'{text}')[0]
        win.activate()
        ttsengine.say(f"focusing on {text}")
        ttsengine.runAndWait()
    except IndexError:
        print("nope")
        ttsengine.say(f"There is no program open named {text}")
        ttsengine.runAndWait()

def shutDown():
    os.startfile(shutDownPath)

def extract():
    hotkey("win", "ctrl", "2")
    hotkey("shiftleft", "shiftright", "f10")
    press("t")
    press("enter")

def newFolder():
    hotkey("ctrl", "shiftleft", "shiftright", "n")

def undo():
    hotkey("ctrl", "z")

def redo():
    hotkey("ctrl", "y")

def copy():
    hotkey("ctrl", "c")

def cut():
    hotkey("ctrl", "x")

def paste():
    hotkey("ctrl", "v")

# ----- MINECRAFT ----- #

def runNewestModrinth():
    win = gw.getWindowsWithTitle('Modrinth App')[0]
    win.activate()
    click(40,450)
    time.sleep(1)
    click(1350,100)

def modrinthModList():
    win = gw.getWindowsWithTitle('Modrinth App')[0]
    win.activate()
    click(40,450)
    time.sleep(1)
    click(1350,300)

def minecraftOptions():
    press("esc")
    click(600, 600)

# ----- GOOGLE ----- #

def searchGoogle(text):
    win = gw.getWindowsWithTitle(f'{browser}')[0]
    win.activate()
    hotkey("ctrl", "t")
    typewrite(f"{text}")
    press("a")
    press("backspace")
    press("enter")

def closeGoogleTab():
    win = gw.getWindowsWithTitle(f'{browser}')[0]
    win.activate()
    hotkey("ctrl", "w")

def searchYoutube(text):
    win = gw.getWindowsWithTitle(f'{browser}')[0]
    win.activate()
    hotkey("ctrl", "t")
    typewrite(f"you")
    press("enter")
    time.sleep(2.2)
    click(600,150)
    typewrite(f"{text}")
    time.sleep(2.2)
    press("enter")

def newTab():
    win = gw.getWindowsWithTitle(f'{browser}')[0]
    win.activate()
    hotkey("ctrl", "t")

# ----- DISCORD ----- #

def answerCall():
    win = gw.getWindowsWithTitle('Discord')[0]
    win.activate()
    hotkey("ctrl", "enter")

def readIncomingDM():
    win = gw.getWindowsWithTitle('Discord')[0]
    win.activate()
    hotkey("ctrl", "1")
    time.sleep(0.3)
    hotkey("ctrl", "1")
    time.sleep(0.3)
    hotkey("alt", "shiftleft", "shiftright", "ctrl", "down")

def reply():
    win = gw.getWindowsWithTitle('Discord')[0]
    win.activate()
    press("esc")

def checkCurrentCall():
    win = gw.getWindowsWithTitle('Discord')[0]
    win.activate()
    hotkey("ctrl", "shiftleft", "shiftright", "alt", "v")

def mute():
    win = gw.getWindowsWithTitle('Discord')[0]
    win.activate()
    hotkey("ctrl", "shiftleft", "shiftright", "m")
    hotkey("alt", "tab")

def deafen():
    win = gw.getWindowsWithTitle('Discord')[0]
    win.activate()
    hotkey("ctrl", "shiftleft", "shiftright", "d")
    hotkey("alt", "tab")

def call():
    win = gw.getWindowsWithTitle('Discord')[0]
    win.activate()
    hotkey("ctrl", "'")

def soundboard():
    win = gw.getWindowsWithTitle('Discord')[0]
    win.activate()
    hotkey("ctrl", "shiftleft", "shiftright", "b")

def toggleChat():
    win = gw.getWindowsWithTitle('Discord')[0]
    win.activate()
    hotkey("ctrl", "u")

def searchDiscord():
    win = gw.getWindowsWithTitle('Discord')[0]
    win.activate()
    hotkey("ctrl", "f")

# ----- STEAM ----- #

def steamRefresh():
    ttsengine.say("Refreshing Steam games")
    ttsengine.runAndWait()
    steamGames, steamAppIds = get_games()
    f = open("steamgames.txt", "w")
    for i in range(len(steamGames)):
        try:
            f.write(f"{steamGames[i]} \n")
        except UnicodeEncodeError:
            f.write(f"{steamGames[i][6:]}")
    f.close()
    f = open("steamappids.txt", "w")
    for i in range(len(steamGames)):
        f.write(f"{steamAppIds[i]} \n")
    ttsengine.say("Refreshed Steam games")
    ttsengine.runAndWait()
    return(steamGames, steamAppIds)

def steamRoulette(steamGames):
    ttsengine.say("rolling")
    ttsengine.runAndWait()
    num = random.randint(0,len(steamGames))
    time.sleep(2)
    if steamGames[num].isdecimal():
        ttsengine.say(f"Your Steam game has been stored in selection.txt")
        ttsengine.runAndWait()
    else:
        ttsengine.say(f"Your chosen game is {steamGames[num]}")
        ttsengine.runAndWait()
    f = open("selection.txt", "w")
    f.write(steamGames[num])
    f.close()
    try:
        win = gw.getWindowsWithTitle('Steam Big Picture Mode')[0]
        win.activate()
        time.sleep(0.5)
        click(123, 1051)
        time.sleep(0.5)
        click(165, 380)
        time.sleep(1)
        click(200, 50)
        typewrite(steamGames[num])
        time.sleep(1)
        click(188, 201)
    except IndexError:
        try:
            win = gw.getWindowsWithTitle('Steam')[0]
            win.activate()
            click(232, 59)
            time.sleep(1)
            click(277, 226)
            time.sleep(0.3)
            click(200, 226)
            typewrite(steamGames[num])
            time.sleep(1)
            click(234, 300)
            press("down")
        except:
            pass

def bigPictureMode():
    win = gw.getWindowsWithTitle('Steam')[0]
    win.activate()
    click(116, 16)
    time.sleep(0.1)
    click(171, 254)

def reviewScoreLast():
    name, score = get_review_score_last()
    if name != "none":
        ttsengine.say(f"Your game {name} has a review score of {score}")
        ttsengine.runAndWait()

def descriptionLast():
    name, description = get_description_last()
    if name != "none":
        ttsengine.say(f"Your game {name}'s description is: {description}")
        ttsengine.runAndWait()

# ----- HELP ----- #

def listCommands():
    press("win")
    time.sleep(0.1)
    typewrite("notepad")
    press("enter")
    time.sleep(0.2)
    hotkey("ctrl", "win", "up")
    typewrite("So, you asked for help.")
    press("enter")
    press("enter")
    typewrite("# ----- DESKTOP UTILITIES ----- #")
    press("enter")
    press("enter")
    typewrite("close/kill - Closes a running program.")
    press("enter")
    typewrite("copy - Copies a file, folder, or text.")
    press("enter")
    typewrite("cut - Cuts a file, folder, or text.")
    press("enter")
    typewrite("extract - Extracts the focused zip file.")
    press("enter")
    typewrite("focus - Focuses on a window.")
    press("enter")
    typewrite("fullscreen - Fullscreens the application.")
    press("enter")
    typewrite("new folder - Creates a new folder in the focused window.")
    press("enter")
    typewrite("open/run - Runs a program.")
    press("enter")
    typewrite("paste - Pastes a file, folder, or text.")
    press("enter")
    typewrite("redo - Redoes an action.")
    press("enter")
    typewrite("screenshot - Screenshots the screen and saves it to my source folder.")
    press("enter")
    typewrite("shut down - Shuts down the PC.")
    press("enter")
    typewrite("switch window (left/right) - Switches the window to another desktop.")
    press("enter")
    typewrite("undo - Undoes an action.")
    press("enter")
    press("enter")
    typewrite("# ----- MINECRAFT ----- #")
    press("enter")
    press("enter")
    typewrite("open Minecraft modlist - Opens the modlist of the last instance used.")
    press("enter")
    typewrite("Minecraft options - Opens Minecraft options.")
    press("enter")
    typewrite("run newest Minecraft - Focuses on Modrinth and runs the last instance used.")
    press("enter")
    press("enter")
    typewrite("# ----- BROWSERS ----- #")
    press("enter")
    press("enter")
    typewrite("close tab - Closes a tab.")
    press("enter")
    typewrite("new tab - Opens a new tab.")
    press("enter")
    typewrite("search - Searches on the browser in config.json.")
    press("enter")
    typewrite("YouTube - Searches on YouTube.")
    press("enter")
    press("enter")
    typewrite("# ----- DISCORD ----- #")
    press("enter")
    press("enter")
    typewrite("answer call - Answers a Discord call.")
    press("enter")
    typewrite("call - Calls the currently focused group/DM.")
    press("enter")
    typewrite("chat - Toggles chat in a Discord call.")
    press("enter")
    typewrite("check current call - Navigates to the current call you're in.")
    press("enter")
    typewrite("check DM - Checks the last thing you were mentioned in.")
    press("enter")
    typewrite("deafen - Deafens the call you're in.")
    press("enter")
    typewrite("mute - Mutes your mic.")
    press("enter")
    typewrite("reply - Replies to the currently focused Discord channel.")
    press("enter")
    typewrite("search Discord - Searches the current Discord channel.")
    press("enter")
    typewrite("soundboard - Activates the soundboard.")
    press("enter")
    press("enter")
    typewrite("# ----- STEAM ----- #")
    press("enter")
    press("enter")
    typewrite("Big Picture Mode - Enables Steam Big Picture Mode")
    press("enter")
    typewrite("description - Gets the short description of your last played game.")
    press("enter")
    typewrite("game roulette - Picks a random Steam game you own.")
    press("enter")
    typewrite("review score - Gets the review score of your last played game.")
    press("enter")
    typewrite("Steam refresh - Refreshes your list of Steam games.")
    press("enter")
    press("enter")
    typewrite("# ----- DICTATION MODE ----- #")
    press("enter")
    press("enter")
    typewrite("dictation mode - Enters Dictation Mode.")
    press("enter")
    typewrite("exit dictation - Exits Dictation Mode.")

### --- MAIN CODE --- ###



while True:
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source,duration=1)
            print("Listening...")

            audio = r.listen(source)
            print(r.recognize_google(audio))
            text = r.recognize_google(audio)
            if dictation == False and respond == False:
                if text.startswith("Lancer "):
                    text = text[7:]
                    if text == "close tab":
                        closeGoogleTab()
                        ttsengine.say(f"closing tab")
                        ttsengine.runAndWait()
                    elif text == "new tab":
                        newTab()
                        ttsengine.say(f"Opening a new tab")
                        ttsengine.runAndWait()
                    elif text == "undo":
                        undo()
                        ttsengine.say("Undoing previous action")
                        ttsengine.runAndWait()
                    elif text == "redo":
                        redo()
                        ttsengine.say("Redoing previous action")
                        ttsengine.runAndWait()
                    elif text == "copy":
                        copy()
                        ttsengine.say("Copying")
                        ttsengine.runAndWait()
                    elif text == "cut":
                        cut()
                        ttsengine.say("Cutting")
                        ttsengine.runAndWait()
                    elif text == "paste" or text == "pace":
                        paste()
                        ttsengine.say("Pasting")
                        ttsengine.runAndWait()
                    elif text == "steam refresh":
                        steamList, steamAppIdList = steamRefresh()
                    elif text == "game roulette":
                        steamRoulette(steamList)
                    elif text == "Big Picture Mode":
                        bigPictureMode()
                        ttsengine.say("Enabling Big Picture Mode")
                        ttsengine.runAndWait()
                    elif text == "review score":
                        reviewScoreLast()
                    elif text == "description":
                        descriptionLast()
                    elif text.startswith("YouTube "):
                        text = text[8:]
                        searchYoutube(text)
                        ttsengine.say(f"searching Youtube for {text}")
                        ttsengine.runAndWait()
                    elif text == "switch window left":
                        windowSwitchLeft()
                        ttsengine.say(f"switching window left")
                        ttsengine.runAndWait()
                    elif text == "switch window right":
                        windowSwitchRight()
                        ttsengine.say(f"switch window right")
                        ttsengine.runAndWait()
                    elif text == "extract":
                        extract()
                        ttsengine.say("extracting zip file")
                        ttsengine.runAndWait()
                    elif text == "new folder":
                        newFolder()
                        ttsengine.say("Creating a new folder")
                        ttsengine.runAndWait()
                    elif text == "full screen":
                        fullscreen()
                        ttsengine.say(f"full screening application")
                        ttsengine.runAndWait()
                    elif text.startswith("Focus "):
                        text = text[6:]
                        focus(text)
                    elif text == "screenshot":
                        takeAScreenshot()
                        ttsengine.say(f"taking a screenshot", "Taking a screenshot")
                        ttsengine.runAndWait()
                    elif text.startswith("run newest Minecraft"):
                        runNewestModrinth()
                        ttsengine.say(f"running your recently played Minecraft")
                        ttsengine.runAndWait()
                    elif text == "open Minecraft mod list":
                        modrinthModList()
                        ttsengine.say("Opening Mod List")
                        ttsengine.runAndWait()
                    elif text == "Minecraft options":
                        minecraftOptions()
                        ttsengine.say("Opening Minecraft Options")
                        ttsengine.runAndWait()
                    elif text.startswith("run ") or text.startswith("Run "):
                        text = text[4:]
                        text = text.title()
                        runProgram(text)
                    elif text.startswith("open "):
                        text = text[5:]
                        text = text.replace(" ", "")
                        text = text.title()
                        runProgram(text)
                    elif text.startswith("check DM"):
                        readIncomingDM()
                        ttsengine.say("Reading new DM")
                        ttsengine.runAndWait()
                    elif text.startswith("answer call"):
                        answerCall()
                        ttsengine.say("Answering call")
                        ttsengine.runAndWait()
                    elif text.startswith("check current call"):
                        checkCurrentCall()
                        ttsengine.say("Checking current call")
                        ttsengine.runAndWait()
                    elif text == "mute":
                        mute()
                        ttsengine.say("Muting microphone")
                        ttsengine.runAndWait()
                    elif text == "deafen" or text == "deaf" or text == "definition" or text == "death":
                        deafen()
                        ttsengine.say("Deafening call")
                        ttsengine.runAndWait()
                    elif text == "call":
                        call()
                        ttsengine.say("Calling DM")
                        ttsengine.runAndWait()
                    elif text == "soundboard":
                        soundboard()
                        ttsengine.say("Activating Soundboard")
                        ttsengine.runAndWait()
                    elif text == "chat":
                        toggleChat()
                        ttsengine.say("Toggling chat")
                        ttsengine.runAndWait()
                    elif text == "search discord":
                        searchDiscord()
                        ttsengine.say("Searching Discord channel")
                        ttsengine.runAndWait()
                    elif text == "dictation mode":
                        dictation = True
                        ttsengine.say("turning on Dictation Mode")
                        ttsengine.runAndWait()
                    elif text == "reply":
                        reply()
                        respond = True
                        ttsengine.say("What will you say?")
                        ttsengine.runAndWait()
                        typewrite("reply")
                        time.sleep(0.3)
                        hotkey("ctrl", "backspace")
                    elif text.startswith("close "):
                        text = text[6:]
                        text = text.replace(" ", "")
                        text = text.title()
                        killProgram(text)
                        ttsengine.say(f"closing {text}")
                        ttsengine.runAndWait()
                    elif text.startswith("kill "):
                        text = text[5:]
                        text = text.replace(" ", "")
                        text = text.title()
                        killProgram(text)
                        ttsengine.say(f"killing {text}")
                        ttsengine.runAndWait()
                    elif text == "help" or text == "list commands" or text == "health":
                        ttsengine.say("Listing commands")
                        ttsengine.runAndWait()
                        listCommands()
                    elif text == "shut down":
                        ttsengine.say("Shutting down")
                        ttsengine.runAndWait()
                        shutDown()
                    elif text.startswith("search up "):
                        text = text[10:]
                        searchGoogle(text)
                        ttsengine.say(f"searching {text}")
                        ttsengine.runAndWait()
                    elif text.startswith("search "):
                        text = text[7:]
                        searchGoogle(text)
                        ttsengine.say(f"searching {text}")
                        ttsengine.runAndWait()
                if text == "Lancer":
                    ttsengine.say("What can I do for you?")
                    ttsengine.runAndWait()
            elif dictation == True:
                if text == "Lancer exit dictation":
                    dictation = False
                    ttsengine.say("Exiting Dictation Mode")
                    ttsengine.runAndWait()
                else:
                    typewrite(text)
            elif respond == True:
                typewrite(text)
                press("enter")
                ttsengine.say(f"Replying with {text}")
                ttsengine.runAndWait()
                respond = False
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("Could not understand audio")

    except KeyboardInterrupt:
        print("Program terminated by user")
        ttsengine.say("This is too much for me!")
        ttsengine.runAndWait()
        break
        
            
    

