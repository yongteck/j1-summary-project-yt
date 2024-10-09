import entities
import gamedata


class ItemEffect:
    """An in-game item effect.

    Items are distinct from Actions in two ways:
    - Items only affect the item owner.
    - Item effects are fixed-value boosts to stats, and do not involve
      multipliers or other complicated calculations.
    """
    name: str
    description: str

    def __init__(self, change: dict[str, int]):
        """Changes are represented as python dicts.
        Keys: hp, maxhp, attack, defense, sanity
        Values: int

        Arguments
        ---------
        + change: dict[str, int]
          The change to apply to the item owner.
        """
        self.change = change

    def __str__(self):
        return self.name

    def apply_effect(self, entity: entities.Entity) -> None:
        """Applies the effect of this item to the entity."""
        for stat, value in self.change.items():
            if stat == "maxhp":
                entity.stats.maxhp += value
            elif stat == "hp":
                if value >= 0:
                    entity.heal(value)
                else:
                    entity.take_hit(value)
            else:
                # Update the stats object attribute
                setattr(entity.stats, stat, getattr(entity.stats, stat) + value)


class Item:

    def __init__(self, name, descriptions, effects, states):
        self.name = name
        self.description = descriptions
        self.effects = effects
        self.states = states

    def check_description(self):
        return self.description

    def check_effects(self):
        return self.effects

    def check_states(self):
        return self.states

    def set_descriptions(self, description):
        self.description = description

    def set_effects(self, effect):
        self.effects = effect

    def set_states(self, state):
        self.states = state


class Inventory:

    def __init__(self):
        self.bag = []

    def add_item(self, item):
        if len(self.bag) == 5:
            print("bag is full")
            return False
        else:
            self.bag.append(item)

    def remove_item(self, item):
        new, seen = [], False
        for i in self.bag:
            if not seen and i == item:
                seen = True
            else:
                new += i
        self.bag = new

    def display(self):
        print("inventory contains " + str([i.name for i in self.bag]))

    def get_item_effects(self) -> list[str]:
        effects = set()
        for bag_item in self.bag:
            for effect in bag_item.check_effects():
                effects.add(effect)
        return list(effects)


def create_item(name: str) -> Item:
    itemdata = gamedata.items[name]
    return Item(itemdata["name"], itemdata["description"], itemdata["effects"], itemdata["states"])

def create_item_effect(name: str) -> ItemEffect:
    itemeffectdata = gamedata.itemeffects[name]
    return ItemEffect(itemeffectdata)
