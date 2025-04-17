class Deck:
    def __init__(self, title="Untitled Deck"):
        self.title = title
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self, front_text):
        self.cards = [card for card in self.cards if card.front != front_text]

    def get_card(self, index):
        if 0 <= index < len(self.cards):
            return self.cards[index]
        return None

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def list_cards(self):
        for i, card in enumerate(self.cards):
            print(f"{i + 1}. {card.front}")