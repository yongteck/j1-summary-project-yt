# Import statements
#yt
class Entity:
    def __init__(self):
        self.hp = 10
        self.atk = 10

#jayden
class Game:
    def __init__(self):
        print("game has started")
        self.ended = False
        self.phase = "explore"
        self.player = Player()
        self.roomdata = {
            "hallway":
            {
                "description":"its a hallway"
            }
            ,"dining room":
            {
                "description":"people eat in this dining room"
            }
        }

    def isover(self):
        return self.ended

    def CheckNode(self,room):
        return self.roomdata[room]

    def gameloop(self):
        print("game is running")
        
        if self.phase == "explore":
            print("at node: ",self.player.playerpos)
        elif self.phase == "battle":
            print("fighting now")
        elif self.phase == "event":
            print("kaydn bum event")

    
#jayden
if __name__ == "__main__":
    print("skibidi toilet")
    game = Game()
    while not game.isover():
        game.gameloop()


#kaydn

#xinyu

