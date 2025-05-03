import random                    # made random global
import card as card_class
import readWrite


class Deck:
    def __init__(self, title="Untitled Deck"):
        """
        :param title: if it has a .txt extension, tries to read in a file of that name, otherwise makes a new deck
        :type title: str
        """
        self.__cards = []   # made attributes private

        # case 1: the user passes a text file to be read in as the title
        try:
            Deck.readable_as_deck(title)
            lines = readWrite.readByLine(title)[1:-1]        # first line is the deck flag
            # code below only executes if the title was successfully read as a text file
            self.__title = title[:-4]                        # i.e., the filename minus the extension
            for i in range(len(lines)):
                if lines[i] != '\n':
                    print(lines[i].split(':'))
                    front, back = lines[i].split(":")            # convert each line of plain text to a card
                    card = card_class.Card(card_class.Card.restore(front), card_class.Card.restore(back))
                    self.add_card(card)
            print(f"Read a deck in existing deck {self.__title}.")

        # case 2: the user is making a new deck and passes the title they want it to have
        except FileNotFoundError as wtf:
            print(wtf)
            if title[-4:] == '.txt':
                self.__title = title[:-4]
            else:
                self.__title = title
            print(f"Instantiated a new deck {self.__title}.")

    def __len__(self):
        return len(self.__cards)

    def add_card(self, card):
        self.__cards.append(card)

    def remove_card(self, front_text):
        self.__cards = [card for card in self.__cards if card.get_front() != front_text]

    def get_card(self, index):
        if 0 <= index < len(self.__cards):
            return self.__cards[index]
        return None

    def shuffle(self):
        random.shuffle(self.__cards)

    def list_cards(self):
        for i, card in enumerate(self.__cards):
            print(f"{i + 1}. {card.get_front()} | {card.get_back()}")

    # added a set cards method
    def set_card(self, index, front, back):
        self.__cards[index].set_front(front)
        self.__cards[index].set_back(back)

    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    # static method to see if a text file can be read as a deck
    @staticmethod
    def readable_as_deck(filename):
        """
        :type filename: str
        :rtype: NoneType
        :raises: FileNotFoundError
        """
        lines = readWrite.readByLine(filename)                                      # lst[str]
        first_line = lines[0]                                                       # str
        if first_line != "can be read as a valid deck\n":                           # raise an exception of no flag
            raise FileNotFoundError(f"No such deck file: '{filename}'")

    def store(self):
        """
        Writes deck to text file title.txt.
        """
        content = "can be read as a valid deck\n"                                   # str
        # each card becomes a line in the text file, front:back
        for i in range(len(self.__cards)):                                          # int
            content +=\
                (f"{card_class.Card.validify(self.__cards[i].get_front())}:"
                 f"{card_class.Card.validify(self.__cards[i].get_back())}\n")
        readWrite.writeToFile(content, f"{self.__title}.txt")

    def delete(self):
        readWrite.deleteFile(f"{self.__title}.txt")

    def __str__(self):
        result = ''
        for i in range(len(self.__cards)):
            result += f'{self.__cards[i].get_front()}:{self.__cards[i].get_back()}\n'
        return result

def main():
    deck = Deck("Math")
    deck.store()
    deck = Deck("Math.txt")
    deck.delete()
    deck = Deck("Math.txt")
    print(deck.get_title())


if __name__ == '__main__':
    main()
