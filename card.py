class Card:
    def __init__(self, front, back):
        # made attributes private. m
        self.__front = front  # Question or term
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
