

class Room:
    def __init__(self, type, id, nexts, monsters, items):
        self.type = type
        self.id = id
        self.nexts = nexts # List of next rooms to choose from
        self.next = None # Actual choice of the player
        self.monsters = monsters
        self.items = items

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

class Map:
    def __init__(self, head):
        self.current = head
    def GetNextRooms(self):
        return self.current.nexts
    def GoNextRoom(self, roomId):
        self.current = roomId
    def GetRoomData(self):
        return [self.current.CheckRoomType(), self.current.CheckRoomMonsters(), self.current.CheckRoomItems()]

