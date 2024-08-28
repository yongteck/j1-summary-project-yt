class Room:

    def __init__(self, type, description, id, monsters, items, next_rooms):
        self.type = type
        self.id = id
        self.nexts = next_rooms  # List of next rooms to choose from
        self.monsters = monsters
        self.items = items
        self.description = description

    def CheckRoomType(self):
        return self.type

    def CheckRoomId(self):
        return self.id

    def CheckNextRooms(self):
        return self.nexts

    def CheckRoomMonsters(self):
        return self.monsters

    def CheckRoomItems(self):
        return self.items


class Map:

    def __init__(self):
        self.store = {}
        self.store["1"] = Room("explore", "tutorial stage", "1", "", [],
                               ["2", "3"])
        self.store["2"] = Room("fgalter", "false god's alter", "2", "", [],
                               ["4"])
        self.store["3"] = Room("combat", "bedroom", "3", "goblin",
                               ["wooden sword"], ["4"])
        self.store["4"] = Room("treasure", "kings bedroom", "4", "",
                               ["wooden shield", "pendant"], ["6", "5"])
        self.store["5"] = Room("library1", "a dilpaitated library", "5", "",
                               [], ["6", "7"])
        self.store["6"] = Room("combat", "hallway", "6", "lebron james", [],
                               ["7"])
        self.store["7"] = Room("campfire", "a moment of respite", "7", "", [],
                               ["6", "8"])
        self.store["8"] = Room("combat", "dungeon", "5", "ny math homework",
                               [], ["1"])

    def update_room(self, obj):
        self.store[obj.CheckRoomId()] = obj

    def getRoom(self, id):
        return self.store[id]


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
