class Player:
    """
    Class representing the players of Hanabi

    This class is used to show each player
    """

    def __init__(self, game, name, hand):
        self.game = game
        self.name = name
        self.hand = hand
        self.known = [{'type': False, 'color': False} for i in range(len(hand))]
        print(self.known)
        pass

    def discard(self, index):
        pass

    def play(self, index):
        pass

    def draw(self):
        pass

    def _get_hint(self, indices, type):
        pass