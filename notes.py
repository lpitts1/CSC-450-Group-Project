# John Keenan
# 4/13/25
# CSC450-002
# Professor Devon Simmonds
# Notes class
import readWrite


class Notes:
    """
    A class composed of a title, and a body string, with functionality to read from and write to textfiles.
    """
    def __init__(self, title, body="LOAD"):
        """
        Constructor.
        :param title: str   will be the name of the textfile stored
        :param body: str    the notes content; optional parameter. If not passed, will try to open <title>.txt, and its
                            contents will be the body
        """
        self.__title = title
        if body == "LOAD":              # the default value of the body parameter
            try:
                self.__body = readWrite.readFromFile(f'{title}.txt')  # read in the file with that name
                self.__body = self.__body[self.__body.index('\n') + 1:]    # delete the first line
            except FileNotFoundError:
                print("it's fine life isn't hopeless or anything")
                self.__body = ""
        else:
            self.__body = body

    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def get_body(self):
        return self.__body

    def set_body(self, body):
        self.__body = body

    def __is_valid_deck(self):
        """
        Private function, used when storing.
        :return:
        """
        lines = self.__body.split("\n")
        for line in lines:
            if line != '':
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
        readWrite.writeToFile(f"""can{"" if self.__is_valid_deck() else "not"} be read as a valid deck
{self.__body}""", f"{self.__title}.txt")

    def __str__(self):
        return self.__body

    def delete(self):
        """
        Deletes the file.
        :return: nothing
        """
        readWrite.deleteFile(f"{self.__title}.txt")


def main():
    s0 = 's0'
    n = Notes(s0)
    print(n.get_title(), n.get_body())

if __name__ == '__main__':
    main()
