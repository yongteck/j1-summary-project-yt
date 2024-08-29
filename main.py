# Import statements
from game import Game
from rooms import Map, Dialogue
from entities import Pokedex, Moveset
from inventory import Itemref


def main(game):
    print("game is running")
    current = "1"
    _map = Map()
    _dex = Pokedex()
    _refr = Itemref()
    dlg = Dialogue()
    ms = Moveset()
    while game.phase != "end":
        room = _map.getRoom(current)
        print("-------\n\n-------")
        print("you are in room: ", room.CheckRoomId(), "type: ", room.type)
        print(room.description)
        print()
        #change effects based off items
        game.player.effects = []
        for bag_item in game.inventory.bag:
            game.player.add_effects(bag_item.check_effects())
        #reset stats due to effects
        game.player.currattack = game.player.attack
        game.player.currsanity = game.player.sanity
        game.shield = 0
        #change stats based off effects
        for eff in game.player.effects:
            if eff == "sharp":
                game.player.currattack += 2
            if eff == "sane":
                game.player.currsanity += 5
            if eff == "guarded":
                game.player.shield += 5

        #combat room
        if room.CheckRoomType() == "combat":
            print("you have entered a combat room")
            monster = _dex.getMonster(room.CheckRoomMonsters())
            turn = "player"
            while True:
                #display
                game.player.displaystats()
                monster.displaystats()
                #player turn
                if turn == "player":
                    choice = input("choose moves: " +
                                   str(game.player.getmoves("P")))
                    turn = "monster"
                    print(ms.getdesc(choice))
                    if choice == "hit":
                        monster.take_hit(game.player.currattack)
                    if choice == "defend":
                        game.player.shield += game.player.maxhp // 2
                    if choice == "adaptation":
                        game.player.currattack += 2
                #monsters turn
                elif turn == "monster":
                    choice = monster.getmoves("M")
                    print("monster chose to:", choice)
                    print(ms.getdesc(choice))
                    turn = "player"
                    if choice == "hit":
                        game.player.take_hit(monster.currattack)
                    if choice == "defend":
                        monster.shield += monster.maxhp // 2
                    if choice == "trip":
                        monster.take_hit(1)
                    if choice == "integration x1.5":
                        monster.currattack = monster.currattack * 1.5 // 1
                        monster.heal(monster.hp // 2)
                    if choice == "slamdunk":
                        game.player.hp -= monster.currattack
                        game.player.sanity -= 1
                if game.player.hp < 1:
                    game.phase = "end"
                    break
                if monster.hp < 1:
                    print("you won the fight")
                    room.type = "explore"
                    game.phase = "rewards"
                    break
                print()
                print()

        #treasure room code
        if room.CheckRoomType() == "treasure":
            game.phase = "rewards"
        if game.phase == "rewards":
            if room.CheckRoomItems == []:
                print("room has already rewarded")
            else:
                print("rewarding")
                for item in room.CheckRoomItems():
                    print("you got {}".format(item))
                    game.inventory.add_item(_refr.get_item(item))
                    room.items = []
                game.phase = "explore"

        #event rooms code
        if room.type == "fgalter":
            choice = input("will you sacrifice blood? (y/n)")
            if choice == "y":
                game.player.sacrifice(5)
                game.player.attack += 1
                game.player.sanity -= 4
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
                    game.player.sanity -= 4
                    game.player.add_moves([choice])
                    books.remove(choice)
            room.type = "explore"

        #campfire code
        if room.type == "campfire":
            print(dlg.getlog("campfire"))
            game.player.hp = game.player.maxhp
            game.player.sanity += 1
            room.type = "explore"

        #looking at new rooms and inventory access
        choice = input("will you access inventory(i) or leave(l)")
        while True:
            if choice == "i":
                game.inventory.display()
                game.player.displayeffects()
                game.player.displaystats()
            elif choice == "l":
                print("choose which room to go to: ")
                for i in room.CheckNextRooms():
                    print("- " + i)
                current = input("Enter your choice: ")
            _map.update_room(room)
            break

    
#jayden
if __name__ == "__main__":
    _game = Game()
    main(_game)

#kaydn

#xinyu
