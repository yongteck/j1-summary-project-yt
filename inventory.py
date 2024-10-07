import gamedata

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


# class Itemref:

#     def __init__(self):
#         self.store = {}
#         self.store["wooden sword"] = Item("wooden sword",
#                                           "a trusty wooden blade", ["sharp"],
#                                           "")
#         self.store["wooden shield"] = Item("wooden shield",
#                                            "a basic defensive tool",
#                                            ["guarded"], "")
#         self.store["pendant"] = Item("pendant",
#                                      "a locket with a blurred photo inside",
#                                      ["sane"], "")

#     def get_item(self, itemname):
#         return self.store[itemname]


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
