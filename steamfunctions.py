import requests
import json
from pyautogui import typewrite, hotkey, press
import pygetwindow as gw
import time
import win32clipboard
import pathlib
import os

web_api_refreshed = 0
runPath = str(pathlib.Path.home() / "AppData/Roaming/Microsoft/Windows/Start Menu/Programs/")
runList = list(runPath)
for i in range(len(runList)):
    if runList[i] == "\\":
        runList[i] = "/"
runList.append("/")
runPath = ''.join(runList)


with open('config.json') as config_file:
    config = json.load(config_file)
    
    api_key = config["api_key"]
    user_id = config["user_id"]

web_api = ""

def refreshWEBAPI():
    global web_api_refreshed
    if web_api_refreshed == 0:
        try:
            win = gw.getWindowsWithTitle('Google Chrome')[0]
            win.activate()
            hotkey("ctrl", "t")
        except IndexError:
            os.startfile(f"{runPath}Google Chrome.lnk")
            time.sleep(2)
        typewrite("https://store.steampowered.com/pointssummary/ajaxgetasyncconfig")
        press("enter")
        time.sleep(1.5)
        hotkey("ctrl", "a")
        hotkey("ctrl", "c")
        hotkey("ctrl", "w")
        time.sleep(0.2)
        press("win")
        time.sleep(0.1)
        typewrite("notepad")
        press("enter")
        time.sleep(0.2)
        hotkey("ctrl", "win", "up")
        hotkey("ctrl", "v")
        for i in range(4):
            press("left")
        for i in range(4):
            hotkey("shiftleft", "shiftright", "up")
        for i in range(17):
            hotkey("shiftleft", "shiftright", "right")
        hotkey("ctrl", "c")
        hotkey("ctrl", "w")
        press("right")
        press("enter")
        win32clipboard.OpenClipboard()
        global web_api
        web_api = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        web_api_refreshed = 1

def get_game_library():
    family = True
    url = f"https://api.steampowered.com/IFamilyGroupsService/GetFamilyGroupForUser/v1/?access_token={web_api}"
    response = requests.get(url)
    try:
        data = response.json()
    except requests.exceptions.JSONDecodeError:
        refreshWEBAPI()
        url = f"https://api.steampowered.com/IFamilyGroupsService/GetFamilyGroupForUser/v1/?access_token={web_api}"
        response = requests.get(url)
        data = response.json()

    if "response" in data and data["response"]["is_not_member_of_any_group"] == True:
        family = False

    if "response" in data and "family_groupid" in data["response"]:
        familyid = data["response"]["family_groupid"]
        

    if family == True:
        url = f"https://api.steampowered.com/IFamilyGroupsService/GetSharedLibraryApps/v1/?access_token={web_api}&family_groupid={str(familyid)}&include_own=true"
    if family == False:
        url = f"https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key={api_key}&steamid={str(user_id)}"
    response = requests.get(url)
    data = response.json()

    if "response" in data and "apps" in data["response"]:
        games = data["response"]["apps"]
        return [game["appid"] for game in games], [game["name"] for game in games]
    else:
        return []

def get_games():
    app_ids, game_list = get_game_library()
    return game_list, app_ids

def get_last_played():
    family = True
    url = f"https://api.steampowered.com/IFamilyGroupsService/GetFamilyGroupForUser/v1/?access_token={web_api}"
    response = requests.get(url)
    try:
        data = response.json()
    except requests.exceptions.JSONDecodeError:
        refreshWEBAPI()
        url = f"https://api.steampowered.com/IFamilyGroupsService/GetFamilyGroupForUser/v1/?access_token={web_api}"
        response = requests.get(url)
        data = response.json()

    if "response" in data and data["response"]["is_not_member_of_any_group"] == True:
        family = False
    
    if "response" in data and "family_groupid" in data["response"]:
        familyid = data["response"]["family_groupid"]

    if family == True:
        url = f"https://api.steampowered.com/IFamilyGroupsService/GetSharedLibraryApps/v1/?access_token={web_api}&family_groupid={str(familyid)}&include_own=true"
    if family == False:
        url = f"https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key={api_key}&steamid={str(user_id)}"
    response = requests.get(url)
    data = response.json()
    highest_time = 0
    if "response" in data and "apps" in data["response"]:
        games = data["response"]["apps"]
    for i in range(len(games)):
        if games[i]["rt_last_played"] > highest_time:
            highest_time = games[i]["rt_last_played"]
            highest_id = games[i]["appid"]
    return highest_id


def get_review_score_last():
    app_id = get_last_played()
    url = f"https://store.steampowered.com/api/appdetails?appids={app_id}"
    response = requests.get(url)
    data = response.json()
    
    if data and str(app_id) in data and data[str(app_id)]["success"]:
        name = data[str(app_id)]["data"]["name"]
        review_score = data[str(app_id)]["data"]["metacritic"]["score"] if "metacritic" in data[str(app_id)]["data"] else "N/A"
        return name, review_score
    return "none", 0

def get_description_last():
    app_id = get_last_played()
    url = f"https://store.steampowered.com/api/appdetails?appids={app_id}"
    response = requests.get(url)
    data = response.json()
        
    if data and str(app_id) in data and data[str(app_id)]["success"]:
        name = data[str(app_id)]["data"]["name"]
        description = data[str(app_id)]["data"]["short_description"] if "short_description" in data[str(app_id)]["data"] else "N/A"
        return name, description
    return "none", "none"

if __name__ == "__main__":
    game_list = get_last_played()
    print(game_list)
    pass    