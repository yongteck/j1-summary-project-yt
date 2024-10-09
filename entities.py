import random


class Stats:
    """Encapsulates the stats of an entity"""

    def __init__(self, hp: int, attack: int, sanity: int, shield: int):
        self.hp = hp
        self.maxhp = hp
        self.attack = attack
        self.sanity = sanity
        self.shield = shield

    def copy(self) -> "Stats":
        """Return a copy of the stats"""
        return Stats(self.hp, self.attack, self.sanity, self.shield)


class Entity:

    def __init__(self, name: int, hp: int, attack: int, sanity: int,
                 shield: int, moves: list[str]):
        self.name = name
        self.stats = Stats(hp, attack, sanity, shield)
        self.effects = []
        self.moves = moves
        # Attributes for combat
        self.original_stats = None
        self.in_combat = False

    @property
    def hp(self) -> int:
        return self.stats.hp

    @property
    def maxhp(self) -> int:
        return self.stats.maxhp

    @property
    def attack(self) -> int:
        return self.stats.attack

    @property
    def sanity(self) -> int:
        return self.stats.sanity

    @property
    def shield(self) -> int:
        return self.stats.shield

    def take_hit(self, value):
        if value > self.shield:
            self.stats.hp -= value - self.shield
            self.stats.shield = 0
        else:
            self.stats.shield -= value

    def get_stats(self) -> Stats:
        return self.stats.copy()

    def heal(self, value):
        if self.hp + value > self.maxhp:
            self.stats.hp = self.maxhp
        else:
            self.stats.hp += value

    def sacrifice(self, value):
        if self.hp - value < 1:
            self.stats.hp = 1
        else:
            self.stats.hp -= value

    def add_effects(self, lst):
        self.effects += [i for i in lst if i not in self.effects]

    def remove_effects(self, lst):
        self.effects = [i for i in self.effects if i not in lst]

    def isdead(self) -> bool:
        return self.hp <= 0

    def getmoves(self) -> str:
        """Subclasseses should override this method"""
        raise NotImplementedError

    def add_moves(self, moves):
        self.moves += moves

    def displaystats(self):
        assert self.original_stats
        print(
            "{} - hp: {}/{}, shield: {}, attack: {}/{}, sanity: {}/{}".format(
                self.name, self.hp, self.maxhp, self.shield, self.attack,
                self.original_stats.attack, self.sanity,
                self.original_stats.sanity))

    def displayeffects(self):
        print("effects: " + str(self.effects))

    def enter_combat(self) -> None:
        """Enter combat mode.
        some stats modified during combat will be reset after exiting combat.
        """
        if self.in_combat:
            raise ValueError("Already in combat")
        self.original_stats = self.get_stats()
        self.in_combat = True

    def exit_combat(self) -> None:
        """Exit combat mode, restoring temporary stats."""
        if not self.in_combat:
            raise ValueError("Not in combat")
        assert self.original_stats
        combat_stats, self.stats = self.stats, self.original_stats
        self.in_combat = False
        # Update stats from combat
        self.stats.hp = combat_stats.hp
        self.stats.maxhp = combat_stats.maxhp
        # Attack, sanity, shield do not carry over


class Player(Entity):

    def getmoves(self) -> str:
        moves = ", ".join(self.moves)
        choice = input(f"choose moves {moves}:")
        while choice not in self.moves:
            choice = input(f"choose moves {moves}:")
        return choice


class Monster(Entity):

    def getmoves(self) -> str:
        return random.choice(self.moves)


def create_entity(jsondata: dict) -> Entity:
    """Creates an entity from json data"""
    return Entity(jsondata["name"], jsondata["hp"], jsondata["attack"],
                  jsondata['sanity'], jsondata["shield"], jsondata["moves"])


def create_player(jsondata: dict) -> Entity:
    """Creates an entity from json data"""
    return Player(jsondata["name"], jsondata["hp"], jsondata["attack"],
                  jsondata['sanity'], jsondata["shield"], jsondata["moves"])


def create_monster(jsondata: dict) -> Entity:
    """Creates an entity from json data"""
    return Monster(jsondata["name"], jsondata["hp"], jsondata["attack"],
                   jsondata['sanity'], jsondata["shield"], jsondata["moves"])
