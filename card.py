# Preston Zuniga
# 4/21/25
# CSC450-002
# Professor Devon Simmonds
# Card class
class Card:
    def __init__(self, front, back):
        """
        Constructor.
        :param front: str  will be the contents of the front of the flashcard
        :param back: str   will be the contents of the back of the flashcard
        """
        self.front = front  # Question or term
        self.back = back    # Answer or definition

    def __str__(self):
        return f"Front: {self.front} | Back: {self.back}"

    def getFront(self):
        return self.front

    def getBack(self):
        return self.back

