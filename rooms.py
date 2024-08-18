

class Room:
    def __init__(self, type, id, monsters, items):
        self.type = type
        self.id = id
        self.nexts = {} # List of next rooms to choose from
        self.next = None # Actual choice of the player
        self.monsters = monsters
        self.items = items
        self.next_rooms = {}

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

    def GetNextRoom(self): 
        return self.next

    def init_next_rooms(self):
        self.nexts[1] = [2, 3]
        self.nexts[2] = [3]


class Map:
    def __init__(self, head):
        self.current = head
    def GetNextRooms(self):
        return self.current.nexts[self.current.id]
    def GoNextRoom(self, next_id):
        self.current = Room(self.current.type, next_id, "monsters", "items")
        return self.current
    def GetRoomData(self):
        return [self.current.type, self.current.monsters, self.current.items]


        