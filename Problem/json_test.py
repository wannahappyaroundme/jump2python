import json

with open("myinfo.json") as f:
    data = json.load(f)
    print(type(data))
    print(data)