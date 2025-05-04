class Card:
    """
    A class composed of two strings, with two string-parsing methods for reading from and writing to textfiles.
    """
    def __init__(self, front, back):
        """
        Constructor.
        :param front: front text
        :param back: back text
        """
        self.__front = str(front)  # Question or term
        self.__back = str(back)    # Answer or definition

    def __str__(self):
        """
        To-string function.
        :return: The front and back labeled.
        """
        return f"Front: {self.__front} | Back: {self.__back}"

    def get_front(self):    # changed method names to lowercase because PyCharm complains about that
        """
        Accessor.
        :return: Current front.
        """
        return self.__front

    def get_back(self):
        """
        Accessor.
        :return: Current back.
        """
        return self.__back

    # mutators added
    def set_front(self, front):
        """
        Mutator.
        :param front: New front.
        :return: Nothing.
        """
        self.__front = str(front)

    def set_back(self, back):
        """
        Mutator.
        :param back: New back.
        :return: Nothing.
        """
        self.__back = str(back)

    @staticmethod
    def validify(string):
        """
        Replaces all newlines and colons with paragraph and section symbols respectively.
        :param string: input string
        :return: output string
        """
        return string.replace('\n', '¶').replace(':', '§')

    @staticmethod
    def restore(string):
        """
        replaces all paragraph and section symbols with newlines and colons respectively.
        :param string: input string
        :return: output string
        """
        return string.replace('¶', '\n').replace('§', ':')


def main():
    c = Card(1, 2)

if __name__ == '__main__':
    main()