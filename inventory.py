class item:
    def __init__(self, name ,descriptions, effects, states):
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

    def set_descriptions(self,description):
        self.description = description

    def set_effects(self, effect):
        self.effects = effect

    def set_states(self, state):
        self.states = state

class itemref:
    def __init__(self):
        self.store = {}
        self.store["wooden sword"] = item("wooden sword","a trusty wooden blade", ["sharp"], "")
        self.store["wooden shield"] = item("wooden shield","a basic defensive tool", ["guarded"], "")
        self.store["pendant"] = item("pendant","a locket with a blurred photo inside",["sane"],"")

    def get_item(self, itemname):
        return self.store[itemname]
    
class inventory:
    def __init__(self):
        self.bag = []

    def add_item(self,item):
        if len(self.bag) == 5:
            print("bag is full")
            return False
        else:
            self.bag.append(item)

    def remove_item(self,item):
        new,seen = [],False
        for i in self.bag:
            if not seen and i == item:
                seen = True
            else:
                new += i
        self.bag = new

    def display(self):
        print("inventory contains " + str([i.name for i in self.bag]))

