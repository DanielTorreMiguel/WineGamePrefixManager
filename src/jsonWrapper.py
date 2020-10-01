import json

def openJson(filename):
    with open(filename) as json_file:
        return json.load(json_file)

'''
saves dictonary to file in json format
'''
def saveToJson(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)