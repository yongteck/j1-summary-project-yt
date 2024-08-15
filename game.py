class Game:
    def __init__(self):
        print("game has started")
        self.ended = False
        self.phase = "explore"
        self.player = Player()

    def CheckNode(self,room):
        return room

    def gameloop(self):
        print("game is running")
        while self.phase != "end":

        
            if self.player.isdead:
                self.phase = "end"
                self.end = True
            
            if self.phase == "explore":
                print("at node: ",self.player.playerpos)
                next_rooms = GetNextRooms()
                choice = int(input("Well done. Choose your next rooms: "))
                for i in range(len(next_rooms)):
                    print(f"({i+1}): room {next_rooms[i]}")
                GoNextRoom(choice)
            
            elif self.phase == "battle":
                print("fighting now")
                
            elif self.phase == "event":
                print("kaydn bum event")
            else:
                print("Game ended")

    
