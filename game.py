from rooms import Map, Dialogue
from entities import Entity, Pokedex, Moveset
from inventory import Itemref, Inventory


class Game:

    def __init__(self):
        print("game has started")
        self.phase = "explore"
        self.player = Entity("player", 10, 4, 10, [])
        self.inventory = Inventory()

    def gameloop(self):
        print("game is running")
        current = "1"
        _map = Map()
        _dex = Pokedex()
        _refr = Itemref()
        dlg = Dialogue()
        ms = Moveset()
        while self.phase != "end":
            room = _map.getRoom(current)
            print("-------\n\n-------")
            print("you are in room: ", room.CheckRoomId(), "type: ", room.type)
            print(room.description)
            print()
            #change effects based off items
            self.player.effects = []
            for bag_item in self.inventory.bag:
                self.player.add_effects(bag_item.check_effects())
            #reset stats due to effects
            self.player.currattack = self.player.attack
            self.player.currsanity = self.player.sanity
            self.shield = 0
            #change stats based off effects
            for eff in self.player.effects:
                if eff == "sharp":
                    self.player.currattack += 2
                if eff == "sane":
                    self.player.currsanity += 5
                if eff == "guarded":
                    self.player.shield += 5

            #combat room
            if room.CheckRoomType() == "combat":
                print("you have entered a combat room")
                monster = _dex.getMonster(room.CheckRoomMonsters())
                turn = "player"
                while True:
                    #display
                    self.player.displaystats()
                    monster.displaystats()
                    #player turn
                    if turn == "player":
                        choice = input("choose moves: " +
                                       str(self.player.getmoves("P")))
                        turn = "monster"
                        print(ms.getdesc(choice))
                        if choice == "hit":
                            monster.take_hit(self.player.currattack)
                        if choice == "defend":
                            self.player.shield += self.player.maxhp // 2
                        if choice == "adaptation":
                            self.player.currattack += 2
                    #monsters turn
                    elif turn == "monster":
                        choice = monster.getmoves("M")
                        print("monster chose to:", choice)
                        print(ms.getdesc(choice))
                        turn = "player"
                        if choice == "hit":
                            self.player.take_hit(monster.currattack)
                        if choice == "defend":
                            monster.shield += monster.maxhp // 2
                        if choice == "trip":
                            monster.take_hit(1)
                        if choice == "integration x1.5":
                            monster.currattack = monster.currattack * 1.5 // 1
                            monster.heal(monster.hp // 2)
                        if choice == "slamdunk":
                            self.player.hp -= monster.currattack
                            self.player.sanity -= 1
                    if self.player.hp < 1:
                        self.phase = "end"
                        break
                    if monster.hp < 1:
                        print("you won the fight")
                        room.type = "explore"
                        self.phase = "rewards"
                        break
                    print()
                    print()

            #treasure room code
            if room.CheckRoomType() == "treasure":
                self.phase = "rewards"
            if self.phase == "rewards":
                if room.CheckRoomItems == []:
                    print("room has already rewarded")
                else:
                    print("rewarding")
                    for item in room.CheckRoomItems():
                        print("you got {}".format(item))
                        self.inventory.add_item(_refr.get_item(item))
                        room.items = []
                    self.phase = "explore"

            #event rooms code
            if room.type == "fgalter":
                choice = input("will you sacrifice blood? (y/n)")
                if choice == "y":
                    self.player.sacrifice(5)
                    self.player.attack += 1
                    self.player.sanity -= 4
                    print(dlg.getlog("fgsacrifice"))
                    room.type = "explore"
                else:
                    print(dlg.getlog("fgignore"))
                print()

            #library1 code
            if room.type == "library1":
                print(dlg.getlog("library1"))
                books = ["adaptation", "endread"]
                while True:
                    choice = input("what will you read? " + str(books))
                    if choice == "endread":
                        break
                    else:
                        print(dlg.getlog(choice))
                        self.player.sanity -= 4
                        self.player.add_moves([choice])
                        books.remove(choice)
                room.type = "explore"

            #campfire code
            if room.type == "campfire":
                print(dlg.getlog("campfire"))
                self.player.hp = self.player.maxhp
                self.player.sanity += 1
                room.type = "explore"

            #looking at new rooms and inventory access
            choice = input("will you access inventory(i) or leave(l)")
            while True:
                if choice == "i":
                    self.inventory.display()
                    self.player.displayeffects()
                    self.player.displaystats()
                elif choice == "l":
                    print("choose which room to go to: ")
                    for i in room.CheckNextRooms():
                        print("- " + i)
                    current = input("Enter your choice: ")
                _map.update_room(room)
                break
