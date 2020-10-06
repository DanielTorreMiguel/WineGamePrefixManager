import json
import os
def openJson(filename):
    with open(filename) as json_file:
        return json.load(json_file)

'''
saves dictonary to file in json format
'''
def saveToJson(data, filename):
    home = os.path.expanduser("~")
    configPath = home + "/.config/wgpm"
    if not os.path.exists(configPath):
        os.makedirs(configPath)
        print("config directory created in: "+configPath)
    with open(configPath + "/" + filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)