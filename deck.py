import random                    # made random global
import card as card_class
import readWrite


class Deck:
    def __init__(self, title="Untitled Deck"):
        print("Instantiating a deck.")
        self.__cards = []   # made attributes private

        # case 1: the user passes a text file to be read in as the title
        try:
            print("Checking if textfile name passed.")
            Deck.readable_as_deck(title)
            print("Textfile name passed. Parsing the file.")
            lines = readWrite.readByLine(title)[1:-1]     # first line is the deck flag
            print("File parsed. Parsing individual lines.")
            # code below only executes if the title was successfully read as a text file
            self.__title = title[:-4]   # i.e., the filename minus the extension
            for i in range(len(lines)):
                print(f"Parsing line {i+1}")
                front, back = lines[i].split(":")
                card = card_class.Card(front, back)
                self.add_card(card)
                print(f"Successfully read in {front} | {back}")

        # case 2: the user is making a new deck and passes the title they want it to have
        except FileNotFoundError:
            print("A textfile name was not passed or an error occurred.")
            self.__title = title

    def add_card(self, card):
        self.__cards.append(card)

    def remove_card(self, front_text):
        self.__cards = [card for card in self.__cards if card.front != front_text]

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

    # static method to see if a text file can be read as a deck
    @staticmethod
    def readable_as_deck(filename):
        lines = readWrite.readByLine(filename)
        first_line = lines[0]
        if first_line != "can be read as a valid deck\n":
            raise FileNotFoundError(f"No such deck file: '{filename}'")

    def store(self):
        content = "can be read as a valid deck\n"
        for i in range(len(self.__cards)):
            content += f"{self.__cards[i].get_front}:{self.__cards[i].get_back}"
        readWrite.writeToFile(content, f"{self.__title}.txt")


def main():
    deck = Deck("Math.txt")
    deck.list_cards()


if __name__ == '__main__':
    main()
