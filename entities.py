import random
class Entity:
    def __init__(self,hp,attack,sanity):
        self.hp = hp
        self.maxhp = hp
        self.attack = attack
        self.sanity = sanity
        self.effects = [{"name":"poison"}]
        self.moves = {
            "hit" : {"description":"hit the person"},
            "defend": {"description":"block the attack"}
        }
        
    def change_sanity(self,value):
        self.sanity += value

    def change_attack(self,value):
        self.attack += value

    def change_hp(self,value):
        self.hp += value

    def add_effects(self,lst):
        self.effects += [i for i in lst if i not in self.effects]

    def remove_effects(self,lst):
        self.effects = [i for i in self.effects if i not in lst]

    def isdead(self) -> bool:
        return self.hp <= 0

    def experience_effect(self):
        for effname in self.effects:
            if effname["name"] == "poison":
                self.change_hp(effname["damage"])

    def getmoves(self,person):
        if person == "P":
            return [i for i in self.moves ]
        if person == "M":
            return random.choice(list(self.moves.keys()))

    def usemove(self, move):
        return self.moves[move]["description"]

# player = Entity(10,10,10)
# choice = input(player.getmoves("P"))
# print(player.usemove(choice))

    



