from entities import Entity
from inventory import Inventory


class Game:

    def __init__(self):
        self.phase = "explore"
        self.player = Entity("player", 10, 4, 10, [])
        self.inventory = Inventory()
        self.enemies = {}

    def add_enemy(self, entity: Entity) -> None:
        self.enemies[entity.name] = entity

    def get_enemy(self, name: str) -> Entity:
        return self.enemies[name]
