class Game:
    def __init__(self):
        print("game has started")
        self.ended = False
        self.phase = "explore"
        self.player = Player()

    def isover(self):
        return self.ended

    def CheckNode(self,room):
        return 

    def gameloop(self):
        print("game is running")

        if self.phase == "explore":
            print("at node: ",self.player.playerpos)
        elif self.phase == "battle":
            print("fighting now")
        elif self.phase == "event":
            print("kaydn bum event")
