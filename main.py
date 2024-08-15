# Import statements
from entities import Entities
from game import Game
from rooms import Room, Map
#yt
    
#jayden
if __name__ == "__main__":
    print("skibidi toilet")


#kaydn


#xinyu


class Item:
    def __init__(self, descriptions, effects, states):
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

