from random import shuffle

class Deck:
    """
    Meaningful docstring
    """
    def __init__(self, difficulty):
        self.cards = setup_cards(difficulty)

    def deal(self, num_players):
        """
        Function to deal hands to the players.

        :param: num_players - integer number of players in the game
        :return: a list of lists in form
            [[hand1], [hand2], ...]
            Each hand is a list of cards that player has.

        cards is modified as it is a reference parameter.
        """
        hands = []
        if num_players == 4 or num_players == 5:
            for i in range(num_players):
                hand = []
                for j in range(4):
                    hand.append(self.draw())
                hands.append(hand)
        else:
            for i in range(num_players):
                hand = []
                for j in range(5):
                    hand.append(self.draw())
                hands.append(hand)

        return hands

    def draw(self):
        """
        Function to draw from the deck

        :return: the card drawn by the player
            cards is modified as it is a reference parameter
        """
        return self.cards.pop()

def setup_cards(difficulty):
    """
    Function to create list of cards.
    List will be shuffled into random order.

    Each card is a dict in the format:
        {
            'color': [Color],
            'value': [Value]
        }

    The deck will have the following colors:
        Red
        Blue
        Green
        Yellow
        White

    Each color will have the following values:
        Three 1's
        Two 2's
        Two 3's
        Two 4's
        One 5

    :return: cards - list of shuffled cards
    """

    colors = ['red', 'blue', 'green', 'yellow', 'white']
    cards = []
    for color in colors:
        for i in range(3):
            cards.append({'color': color, 'value': 1})
        for i in range(2):
            cards.append({'color': color, 'value': 2})
            cards.append({'color': color, 'value': 3})
            cards.append({'color': color, 'value': 4})
        cards.append({'color': color, 'value': 5})

    shuffle(cards)

    return cards

def deal_hands(num_players, cards):
    """
    Function to deal hands to the players.

    :param: num_players - integer number of players in the game
    :param: cards - list of card dicts
    :return: a list of lists in form
        [[hand1], [hand2], ...]
        Each hand is a list of cards that player has.

    cards is modified as it is a reference parameter.
    """
    hands = []
    if num_players == 4 or num_players == 5:
        for i in range(num_players):
            hand = []
            for j in range(4):
                hand.append(cards.pop())
            hands.append(hand)
    else:
        for i in range(num_players):
            hand = []
            for j in range(5):
                hand.append(cards.pop())
            hands.append(hand)

    return hands

def draw(cards):
    """
    Function to draw from the deck

    :param: cards - list of cards
    :return: the card drawn by the player
        cards is modified as it is a reference parameter
    """
    return cards.pop()

if __name__ == '__main__':
    deck = setup_cards()
    print(deal_hands(4, deck))