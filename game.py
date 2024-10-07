import entities
import gamedata
from inventory import Inventory


class Game:

    def __init__(self):
        self.phase = "explore"
        self.player = entities.create_player(gamedata.player)
        self.inventory = Inventory()
        self.enemies = {}

    def add_enemy(self, entity: entities.Entity) -> None:
        self.enemies[entity.name] = entity

    def get_enemy(self, name: str) -> entities.Entity:
        return self.enemies[name]
