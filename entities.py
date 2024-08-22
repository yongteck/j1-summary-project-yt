import random
class moveset:
    def __init__(self):
        self.notebook = {}
        self.notebook["hit"] = "it hits"
        self.notebook["defend"] = "it defends"
        self.notebook["trip"] = "it falls onto the ground"
        self.notebook["integration x1.5"] = "enemys polynomial degree increases, amplifying stats by 1.5x"
        self.notebook["adaptation"] = "you comprehend the concepts behind its structure"
        self.notebook["slamdunk"] = "lebron dunks on you aura -1000"

    def getdesc(self,id):
        return self.notebook[id]
        
class Entity:
    def __init__(self,name,hp,attack,sanity,add_move):
        self.name = name
        self.hp = hp
        self.maxhp = hp
        self.attack = attack
        self.currattack = attack
        self.sanity = sanity
        self.currsanity = sanity
        self.shield = 0
        self.effects = []
        self.moves = ["hit","defend"] + add_move

    def take_hit(self,value):
        if value > self.shield:
            self.hp -= value - self.shield
            self.shield = 0
        else:
            self.shield -= value

    def heal(self,value):
        if self.hp + value > self.maxhp:
            self.hp = self.maxhp
        else:
            self.hp += value

    def sacrifice(self,value):
        if self.hp - value < 1:
            self.hp = 1
        else:
            self.hp -= value

    def add_effects(self,lst):
        self.effects += [i for i in lst if i not in self.effects]

    def remove_effects(self,lst):
        self.effects = [i for i in self.effects if i not in lst]

    def isdead(self) -> bool:
        return self.hp <= 0

    def getmoves(self,person):
        if person == "P":
            return [i for i in self.moves ]
        if person == "M":
            return random.choice(self.moves)

    def add_moves(self,moves):
        self.moves += moves

    def displaystats(self):
        print("{} - hp: {}/{}, shield: {}, attack: {}/{}, sanity: {}/{}".format(self.name, self.hp,self.maxhp, self.shield, self.currattack, self.attack, self.currsanity, self.sanity))

    def displayeffects(self):
        print("effects: "+ str(self.effects))
        
class Pokedex:
    def __init__(self):
        self.store = {}
        self.store["goblin"] = Entity("goblin",10,2,5,["trip"])
        self.store["ny math homework"] = Entity("ny math homework",25,3,5,["integration x1.5"])
        self.store["lebron james"] = Entity("lebron james",10,6,20,["slamdunk"])

    def getMonster(self,id):
        return self.store[id]

    



