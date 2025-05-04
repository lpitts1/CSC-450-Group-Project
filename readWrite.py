# Levi Pitts
# CSC 450
# Devon Simmonds
# defines functions for reading from and writing to files

# Read file function, reads entire file with fileName
def readFromFile(fileName):
    """
    Returns the full contents of a registered textfile.
    :param fileName: include .txt extension
    :return: contents of the file
    """
    with open(fileName) as file:  # Open file in read mode
        isReadable(fileName)
        content = file.read()    # Set variable that contains read info
        print("File read and stored successfully")
        return content           # Return read info

# Read file by line function, reads one line of file with fileName
def readByLine(fileName):
    """
    Returns a list of all lines in the file.
    :param fileName: include .txt extension.
    :return: list of lines.
    """
    isReadable(fileName)
    lineList = []                     # List of lines for storing
    with open(fileName) as file:      # Open file in read mode
        while True:
            line = file.readline()    # Read one line of file, return line
            lineList.append(line)     # Add to lineList
            if not line:              # Exception if end of file
                break
    return lineList

# Create file function with desired file name
def newFile(fileName):
    """
    Creates a new file to be used later.
    :param fileName: include .txt extension.
    :return: Nothing.
    """
    try:                        # Creates a file with exception handling
        f = open(fileName, "x") # Open file in X mode, opens file in write mode but throws
        registerFile(fileName)
        f.close()               # FileExistsError if file name already exists
    except FileExistsError:     # Throw excpetion
        print("File already exists.")

# Write to file function, takes in fileName and input arguments
def writeToFile(input, fileName):
    """
    Writes a string to a file
    :param input: string to be written
    :param fileName: file to which to write it
    :return: nothing
    """
    with open(fileName, 'w') as file:     # Open file in Write mode
        file.write(input)                 # Write input to file
    registerFile(fileName)

def writeByLine(input, fileName):
    """
    Takes a list of strings and writes them to a file one by one.
    :param input: A list of strings (newlines NOT added automatically.)
    :param fileName: file to write to (include .txt extension)
    :return:
    """
    with open(fileName, 'w') as file:
        for line in input:
            file.write(line)

def registerFile(fileName):
    """
    Keeps track of files written using this module to control access and allow retrieval.
    :param fileName: file to be registered
    :return: nothing
    """
    try:
        readable_files = readByLine("readable_files.txt")[:-1]  # a text file containing all readable files
    except FileNotFoundError:
        readable_files = []
    if f"{fileName}\n" not in readable_files:
        readable_files.append(f"{fileName}\n")
    # write a new textfile to keep track of other textfiles
    writeByLine(readable_files, "readable_files.txt")

def deleteFile(fileName):
    """
    Remove file from registered list.
    :param fileName:
    :return:
    """
    old_readable_files = readByLine("readable_files.txt")
    new_readable_files = []
    for file in old_readable_files:
        if file.strip("\n") != fileName:
            new_readable_files.append(file)
    writeByLine(new_readable_files, "readable_files.txt")

def isReadable(fileName):
    """
    Throws a FileNotFoundError if the file does not exist in the stored list of filenames.
    :param fileName: file to be checked
    :return: Nothing.
    """
    if fileName != "readable_files.txt" and f"{fileName}\n" not in readByLine("readable_files.txt"):
        raise FileNotFoundError(f"{fileName} does not exist for purposes of this function.")

def getReadableFiles():
    """
    :return: A list of all filenames in the stored list.
    """
    with open("readable_files.txt") as readable_files:
        contents = readable_files.read()
        lines = contents.split('\n')
        return lines[:-1]

def purge():
    """
    Remove all filenames in the stored list.
    :return: nothing
    """
    with open("readable_files.txt", "w") as bye_bye:
        pass

def main():
    purge()

if __name__ == '__main__':
    main()
