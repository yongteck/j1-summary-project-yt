# Import statements
from game import Game
import gamedata
from rooms import Map, Dialogue
from entities import Pokedex, Moveset
from inventory import Itemref

_dex = Pokedex()
_refr = Itemref()
_map = Map()
_map.setFromJson(gamedata.rooms)
dlg = Dialogue()
ms = Moveset()


def show_room_info(room_id, type, description) -> None:
    """Display room information about the given room."""
    print("-------\n\n-------")
    print("you are in room: ", room_id, "type: ", type)
    print(description)
    print()

def update_stats(game):
    """Update player effects and stats"""
    # TODO: Refactor to make effect updates dynamic
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


def enter_combat(game, room):
    """Enter a combat room"""
    monster = _dex.getMonster(room.CheckRoomMonsters())
    turn = "player"
    while True:
        #display
        game.player.displaystats()
        monster.displaystats()
        #player turn
        if turn == "player":
            player_turn(game.player, monster)
            turn = "monster"
        #monsters turn
        elif turn == "monster":
            monster_turn(game.player, monster)
            turn = "player"
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

def player_turn(player, monster):
    """Player's turn in combat"""
    choice = input("choose moves: " +
           str(player.getmoves("P")))
    print(ms.getdesc(choice))
    if choice == "hit":
        monster.take_hit(player.currattack)
    if choice == "defend":
        player.shield += player.maxhp // 2
    if choice == "adaptation":
        player.currattack += 2

def monster_turn(player, monster):
    """Monster's turn in combat"""
    choice = monster.getmoves("M")
    print("monster chose to:", choice)
    print(ms.getdesc(choice))
    if choice == "hit":
        player.take_hit(monster.currattack)
    if choice == "defend":
        monster.shield += monster.maxhp // 2
    if choice == "trip":
        monster.take_hit(1)
    if choice == "integration x1.5":
        monster.currattack = monster.currattack * 1.5 // 1
        monster.heal(monster.hp // 2)
    if choice == "slamdunk":
        player.hp -= monster.currattack
        player.sanity -= 1

def enter_treasure(game, room):
    """Enter a treasure room."""
    game.phase = "rewards"

def gamephase_rewards(game, room):
    """handle rewards phase of game"""
    if room.CheckRoomItems == []:
        print("room has already rewarded")
    else:
        print("rewarding")
        for item in room.CheckRoomItems():
            print("you got {}".format(item))
            game.inventory.add_item(_refr.get_item(item))
            room.items = []
        game.phase = "explore"

def enter_fgalter(game, room):
    """Enter event room"""
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

def enter_library(game, room):
    """Enter library room"""
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

def enter_campfire(game, room):
    """Enter campfire room."""
    print(dlg.getlog("campfire"))
    game.player.hp = game.player.maxhp
    game.player.sanity += 1
    room.type = "explore"

def inventory_or_leave(game, room):
    """Check inventory or go to next room"""
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
    return current

def main(game):
    print("game is running")
    current = "1"
    while game.phase != "end":
        room = _map.getRoom(current)
        show_room_info(room.id, room.type, room.description)

        update_stats(game)
        if room.type == "combat":
            print("you have entered a combat room")
            enter_combat(game, room)
        if room.type == "treasure":
            enter_treasure(game, room)
        if game.phase == "rewards":
            gamephase_rewards(game, room)
        if room.type == "fgalter":
            enter_fgalter(game, room)
        if room.type == "library1":
            enter_library(game, room)
        if room.type == "campfire":
            enter_campfire(game, room)

        current = inventory_or_leave(game, room)


#jayden
if __name__ == "__main__":
    _game = Game()
    main(_game)

#kaydn

#xinyu
