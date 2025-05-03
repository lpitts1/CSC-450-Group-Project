class Card:
    def __init__(self, front, back):
        # made attributes private. m
        self.__front = front # Question or term
        self.__back = back    # Answer or definition

    def __str__(self):
        return f"Front: {self.__front} | Back: {self.__back}"

    def get_front(self):    # changed method names to lowercase because PyCharm complains about that
        return self.__front

    def get_back(self):
        return self.__back

    # mutators added
    def set_front(self, front):
        self.__front = front

    def set_back(self, back):
        self.__back = back

    @staticmethod
    def validify(string):
        return string.replace('\n', '¶').replace(':', '§')

    @staticmethod
    def restore(string):
        return string.replace('¶', '\n').replace('§', ':')


def main():
    string = """1:i
2:ii
3:iii"""
    print(string)
    string = Card.validify(string)
    print(string)
    string = Card.restore(string)
    print(string)


if __name__ == '__main__':
    main()