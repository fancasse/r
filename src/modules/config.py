import json

config = {}
with open('config.json', 'r') as f:
    config = json.load(f)


def getID(game, id):
  if config[game]["custom-client-id"] != "698274476126765086":
    return config[game]["custom-client-id"]
  else:
    return id


def truckMake(game):
  return config[game]["custom-trucks"]
