# John Keenan
# 4/10/25
# CSC450-002
# Dr. Devon Simmonds
# This program parses a string by newline, then by : colon, into a two dimensional list.
def string_parse(string):
    """
    Parses a string by newline, then by : colon, into a two dimensional list.
    :param string: str format %:%(\n%:%)*
    :return: list[list[str format %:%(\n%:%)*]]
    """
    separate_by_line = string.split('\n')   # separate by newline
    for i in range(len(separate_by_line)):
        separate_by_line[i] = separate_by_line[i].split(':')    # separate by :
    return separate_by_line


def main():
    string = """front0: back0
front1: back1
front2: back2"""
    print(string_parse(string))


if __name__ == '__main__':
    main()
