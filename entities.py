import random


class Stats:
    """Encapsulates the stats of an entity"""
    def __init__(self, hp: int, attack: int, sanity: int, shield: int):
        self.hp = hp
        self.maxhp = hp
        self.attack = attack
        self.sanity = sanity
        self.shield = shield


class Moveset:

    def __init__(self):
        self.notebook = {}
        self.notebook["hit"] = "it hits"
        self.notebook["defend"] = "it defends"
        self.notebook["trip"] = "it falls onto the ground"
        self.notebook[
            "integration x1.5"] = "enemys polynomial degree increases, amplifying stats by 1.5x"
        self.notebook[
            "adaptation"] = "you comprehend the concepts behind its structure"
        self.notebook["slamdunk"] = "lebron dunks on you aura -1000"

    def getdesc(self, id):
        return self.notebook[id]


class Entity:

    def __init__(self, name, hp, attack, sanity, shield, moves):
        self.name = name
        self.stats = Stats(hp, attack, sanity, shield)
        # self.hp = hp
        self.maxhp = hp
        # self.attack = attack
        self.currattack = attack
        # self.sanity = sanity
        self.currsanity = sanity
        # self.shield = shield
        self.effects = []
        self.moves = moves

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

    def getmoves(self, person):
        if person == "P":
            return [i for i in self.moves]
        if person == "M":
            return random.choice(self.moves)

    def add_moves(self, moves):
        self.moves += moves

    def displaystats(self):
        print(
            "{} - hp: {}/{}, shield: {}, attack: {}/{}, sanity: {}/{}".format(
                self.name, self.hp, self.maxhp, self.shield, self.currattack,
                self.attack, self.currsanity, self.sanity))

    def displayeffects(self):
        print("effects: " + str(self.effects))


def create_entity(jsondata: dict) -> Entity:
    """Creates an entity from json data"""
    return Entity(jsondata["name"], jsondata["hp"], jsondata["attack"],
                  jsondata['sanity'], jsondata["shield"], jsondata["moves"])
