# John Keenan
# 4/13/25
# CSC450-002
# Professor Devon Simmonds
# Notes class


import readWrite


class Notes:
    def __init__(self, title, body="LOAD"):
        """
        Constructor.
        :param title: str   will be the name of the textfile stored
        :param body: str    the notes content; optional parameter. If not passed, will try to open <title>.txt, and its
                            contents will be the body
        """
        self.title = title
        if body == "LOAD":                  # the default value of the body parameter
            file = readWrite.readByLine(f"{title}.txt")   # open a textfile with a name equal to the title passed

            # populate the body with the contents of the text file
            self.body = ""
            for line in file[1:]:
                self.body += line

        else:
            self.body = body

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_body(self):
        return self.body

    def set_body(self, body):
        self.body = body

    def __is_valid_deck(self):
        """
        Private function, used when storing.
        :return:
        """
        lines = self.body.split("\n")
        for line in lines:
            front_back = line.split(":")

            # a text file can only be read as a deck if each line has a colon
            if len(front_back) != 2:
                return False
        return True

    def store(self):
        """
        save the note to a text file
        :return: NoneType
        """
        # save the note to a file with a name equal to the title
        # the first line of the file will be whether the document can be read as a card or not
        # the remainder of the file will be the notes body
        readWrite.writeToFile(
            f"can{"" if self.__is_valid_deck() else "not"} be read as a valid deck\n{self.body}",
            f"{self.title}.txt"
        )

    def __str__(self):
        return self.body


def main():
    notes = Notes("Math", """1+1: 2
2+2: 4
3+3: 6""")

    print(notes)
    notes.store()

    math_notes = Notes("Math")
    print(notes)


if __name__ == '__main__':
    main()
