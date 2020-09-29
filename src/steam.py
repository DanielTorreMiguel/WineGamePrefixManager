import urllib.request, json 
import requests

url = 'https://api.steampowered.com/ISteamApps/GetAppList/v0002'
global output
def getGameList():
    data = urllib.request.urlopen(url).read()
    output = json.loads(data)
    for item in output["applist"]["apps"]:
        if item["appid"] == 310950:
            print(item["name"])
            return
        #print(item["appid"], item["name"])
    #with open('data.json', 'w', encoding='utf-8') as f:
    #    json.dump(output, f, ensure_ascii=False, indent=4)

def populateGameList(folder):
    pass
