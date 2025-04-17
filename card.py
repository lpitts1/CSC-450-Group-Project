class Card:
    def __init__(self, front, back):
        self.front = front  # Question or term
        self.back = back    # Answer or definition

    def __str__(self):
        return f"Front: {self.front} | Back: {self.back}"

    def getFront(self):
        return self.front

    def getBack(self):
        return self.back

