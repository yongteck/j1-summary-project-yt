from rooms import Room, Map

class Game:
    def __init__(self, player):
        print("game has started")
        self.ended = False
        self.phase = "explore"
        self.player = player

    def CheckNode(self,room):
        return room

    
    def gameloop(self):
        print("game is running")
        current = Room("Exploration", 1, "monsters", "items")
        current.init_next_rooms()
        _map = Map(current)
        while self.phase != "end":
            
            if self.player.isdead():
                self.phase = "end"
                self.end = True
            if self.phase == "explore":
                print("at node: ", current.id)
                next_rooms = _map.GetNextRooms()
                print("Well done. Choose your next rooms: ")
                for i in range(len(next_rooms)):
                    print(f"({i+1}): room {next_rooms[i]}")
                choice = int(input("Enter your choice here: "))
                _map.GoNextRoom(choice)
            
            elif self.phase == "battle":
                print("fighting now")
                
            elif self.phase == "event":
                print("kaydn bum event")
            else:
                print("Game ended")

    
