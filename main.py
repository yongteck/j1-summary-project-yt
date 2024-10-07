# Import statements
from game import Game
import action
import gamedata
from rooms import Map, Dialogue
from entities import Moveset
import entities
from inventory import Itemref

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

def apply_inventory_effects(stats: entities.Stats):
    """Update player stats based on effect of inventory items"""
    # TODO: Refactor to make effect updates dynamic
    effects = game.inventory.get_item_effects()
    #change stats based off effects
    for effect in effects:
        if effect == "sharp":
            stats.attack += 2
        if effect == "sane":
            stats.sanity += 5
        if effect == "guarded":
            stats.shield += 5


def enter_combat(game, room):
    """Enter a combat room"""
    player = game.player
    monsters = room.CheckRoomMonsters()
    # For now there is only one enemy per room
    monster = game.get_enemy(monsters[0])
    player_stat = player.get_stats()
    apply_inventory_effects(player_stat)
    monster_stat = monster.get_stats()
    turn = "player"
    while True:
        #display
        game.player.displaystats()
        monster.displaystats()
        #player turn
        if turn == "player":
            choice = input("choose moves: " +
           str(player.getmoves("P")))
            print(ms.getdesc(choice))
            player_turn(game.player, monster, choice)
            turn = "monster"
        #monsters turn
        elif turn == "monster":
            choice = monster.getmoves("M")
            print("monster chose to:", choice)
            print(ms.getdesc(choice))
            monster_turn(game.player, monster, choice)
            turn = "player"
        if player.isdead():
            game.phase = "end"
            break
        if monster.isdead():
            print("you won the fight")
            room.type = "explore"
            game.phase = "rewards"
            break
        print()
        print()
    player.update(player_stat)
    monster.update(monster_stat)

def player_turn(player_stat, monster_stat, choice):
    """Player's turn in combat"""
    Action = action.get(choice)
    entityAction = Action(player_stat)
    if isinstance(entityAction, action.SelfAction):
        entityAction.apply_effect(player_stat)
    elif isinstance(entityAction, action.OtherAction):
        entityAction.apply_effect(monster_stat)
    else:
        raise ValueError(f"{entityAction}: Invalid action")

def monster_turn(player_stat, monster_stat, choice):
    """Monster's turn in combat"""
    Action = action.get(choice)
    entityAction = Action(monster_stat)
    if isinstance(entityAction, action.SelfAction):
        entityAction.apply_effect(monster_stat)
    elif isinstance(entityAction, action.OtherAction):
        entityAction.apply_effect(player_stat)
    else:
        raise ValueError(f"{entityAction}: Invalid action")

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
    for enemydata in gamedata.enemy.values():
        _game.add_enemy(entities.create_entity(enemydata))
    main(_game)

#kaydn

#xinyu
