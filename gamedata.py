"""gamedata.py

Enables access to game data through the json file
"""

import json

DATAFILE = "gamedata.json"


def load(filename: str) -> dict:
    """Loads game data from a json file"""
    with open(filename, "r") as f:
        data = json.load(f)
    return data

def reload():
    """Reload game data from file"""
    data = load(DATAFILE)
    global player, enemy, effects, rooms
    player = data["player"]
    enemy = data["enemy"]
    effects = data["effects"]
    rooms = data["rooms"]
    items = data["items"]


_data = load(DATAFILE)
player = _data["player"]
enemy = _data["enemy"]
effects = _data["effects"]
rooms = _data["rooms"]
items = _data["items"]
