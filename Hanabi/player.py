# from errors import *
from copy import deepcopy

UNKNOWN_INFO = {'number': False, 'color': False}

class Player:
    """
    Class representing the players of Hanabi

    This class is used to show each player
    """

    def __init__(self, name):
        self.game = None
        self.name = name
        self.hand = []
        self.known = []
        pass

    def deal(self, hand):
        self.hand = hand
        self.known = [deepcopy(UNKNOWN_INFO) for i in range(len(self.hand))]

    def discard(self, index):
        card = self.hand.pop(index)
        self.known.pop(index)
        self.game.discard(card)
        self.draw()

    def play(self, index):
        card = self.hand.pop(index)
        self.known.pop(index)
        self.game.play(card)
        self.draw()

    def draw(self):
        self.hand.append(self.game.draw())
        self.known.append(deepcopy(UNKNOWN_INFO))

    def get_hint(self, indices, info_type):
        for index in indices:
            print(index)
            if info_type == 'color':
                for index in indices:
                    self.known[index]['color'] = True
            elif info_type == 'value':
                print(self.known[index])
                for index in indices:
                    self.known[index]['number'] = True
                print(self.known[index])
            else:
                pass
                # raise InformationTypeError('Information type must be "color" or "number"')

    def give_hint(self, indices, info_type, target):
        information = {'indices': indices, 'type': info_type}
        self.game.give_hint(target, information)
