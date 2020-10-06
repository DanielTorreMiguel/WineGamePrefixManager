import urllib.request, json 
import requests
import os
import jsonWrapper as jw

url = 'https://api.steampowered.com/ISteamApps/GetAppList/v0002' #url with list of all steam apps in json format

'''
Gets a list with all steam games from a json and returns it in dict format

format:
applist
    apps
        id,name
        id,name
        .
        .
        .
'''
def getGameList():
    data = urllib.request.urlopen(url).read()
    output = json.loads(data)
    jw.saveToJson(output, "fullList.json")
    return output

'''
generates a list with initialised wine games from steam
@param folder steamapps folder to scan
'''
def populateGameList(folders):
    fullGameList = getGameList()
    gameDataList = [] #list with initialised wine games
    gameDataListFull = []
    for folder in folders:
        prefixFolder = folder["path"] + "/compatdata" #folder where the prefixes are
        if os.path.isdir(prefixFolder):
            directories = os.listdir(prefixFolder) #get all the prefix folders
            for directory in directories:
                gameDict = {}
                gameDict['prefixFolder'] = prefixFolder+"/"+directory #wine prefix folder
                gameDict["name"] = "placeholder" #game name
                gameDict["appid"] = int(directory) # game steam id
                gameDataList.append(gameDict)
    for item in fullGameList["applist"]["apps"]:
        for app in gameDataList:
            if item["appid"] == app["appid"]:
                app["name"] = item["name"]
                gameDataList.remove(app)
                gameDataListFull.append(app)
    return gameDataListFull
    


def loadGameList():
    gameList = []
    if os.path.isfile('gameList.json'):
        gameList = jw.openJson('gameList.json')
    else:
        if os.path.isfile('folderList.json'): #if file exists
            data = jw.openJson('folderList.json')
            gameList = populateGameList(data)
            jw.saveToJson(gameList, "gameList.json")
    return gameList

