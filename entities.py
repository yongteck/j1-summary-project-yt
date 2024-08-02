class Entities:
    def __init__(self,hp,damage,sanity):
        self.hp = hp
        self.damage = damage
        self.sanity = sanity
        
    def change_sanity(self,value):
        self.sanity += value

    def change_damage(self,value):
        self.damage += value

    def change_hp(self,value):
        self.hp += value