"""rooms.py

Module for room objects
"""

class Room:

    def __init__(self, type, description, id, monsters, items, next_rooms):
        self.type = type
        self.id = id
        self.exits = next_rooms  # List of next rooms to choose from
        self.monsters = monsters
        self.items = items
        self.description = description

    def CheckRoomType(self):
        return self.type

    def CheckRoomId(self):
        return self.id

    def CheckNextRooms(self):
        return self.exits

    def CheckRoomMonsters(self):
        return self.monsters

    def CheckRoomItems(self):
        return self.items


class Map:

    def __init__(self):
        self.store = {}

    def update_room(self, room: Room):
        self.store[room.CheckRoomId()] = room

    def getRoom(self, id):
        return self.store[id]

    def setFromJson(self, data: list):
        for roomdata in data:
            self.store[roomdata["id"]] = Room(
                roomdata["type"],
                roomdata["description"],
                roomdata["id"],
                roomdata["monsters"],
                roomdata["items"],
                roomdata["exits"]
            )


class Dialogue:

    def __init__(self):
        self.book = {
            "fgsacrifice":
            "you slit your hand dripping blood into the bowl\nforeign energy rushes through your muscles\nthe alter crumbles down, becoming unusable",
            "fgignore":
            "you ignore it\nthis might just be the wisest option",
            "library1":
            "an old and worn down library\nit contains some valuable books\nreading them will grant moves\nstaying for long may not be good for the mind",
            "adaptation":
            "you understand how to learn the weaknesses of your enemies\nyou feel weary and pain shoots through your mind",
            "campfire":
            "the warmth of the azure flame permeates your skin\nIn the comfort you fall asleep\nan unknown amount of time passes\nthe flames have died out"
        }

    def getlog(self, id):
        return self.book[id]
