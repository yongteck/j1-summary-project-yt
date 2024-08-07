class Entities:
    def __init__(self,hp,damage,sanity):
        self.hp = hp
        self.damage = damage
        self.sanity = sanity
        self.effects = []
        
    def change_sanity(self,value):
        self.sanity += value

    def change_damage(self,value):
        self.damage += value

    def change_hp(self,value):
        self.hp += value

    def add_effects(self,lst):
        self.effects += [i for i in lst if i not in self.effects]

    def remove_effects(self,lst):
        self.effects = [i for i in self.effects if i not in lst]

