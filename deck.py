# Preston Zuniga
# 4/13/25
# CSC450-002
# Professor Devon Simmonds
# Deck class
class Deck:
    def __init__(self, title="Untitled Deck"):
        """
        Constructor.
        :param title: str  optional parameter; If not passed it names the deck a default title 
        
        """
        self.title = title     #The name of the deck
        self.cards = []        #The array of cards stored in the deck

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self, front_text):
        self.cards = [card for card in self.cards if card.front != front_text]

    def get_card(self, index):
        """
        Private function, used to get a specific card from a deck.
        :return:
        """
        if 0 <= index < len(self.cards):
            return self.cards[index]
        return None

    def shuffle(self):
        """
        Private function, used to shuffle the deck.
        :return:
        """
        import random
        random.shuffle(self.cards)

    def list_cards(self):
        """
        Private function, used to list all cards in a numbered list
        :return:
        """
        for i, card in enumerate(self.cards):
            print(f"{i + 1}. {card.front}")
