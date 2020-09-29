import urllib.request, json 
import requests
import os

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
    return output

'''
generates a list with initialised wine games from steam
@param folder steamapps folder to scan
'''
def populateGameList(folder, fullGameList):
    gameDataList = {} #list with initialised wine games
    numElements = 0 #number of list elements
    prefixFolder = folder + "compatdata" #folder which 
    directories = os.listdir(prefixFolder) #get all the folders in the wine 
    for item in fullGameList["applist"]["apps"]:
        for directory in directories:
            if item["appid"] == int(directory):
                gameDict = {}
                gameDict['prefixFolder'] = prefixFolder+"/"+directory #wine prefix folder
                gameDict["name"] = item["name"] #game name
                gameDict["appid"] = item["appid"]# game steam id
                gameDataList[numElements] = gameDict
                numElements+=1
                directories.remove(directory) #remove it to reduce complexity
    saveToJson(gameDataList, "installed.json")
    
'''
saves dictonary to file in json format
'''
def saveToJson(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)