# Levi Pitts
# CSC 450
# Devon Simmonds
# defines functions for reading from and writing to files

# Read file function, reads entire file with fileName
def readFromFile(fileName):
    with open(fileName) as file: # Open file in read mode
        isReadable(fileName)
        content = file.read()    # Set variable that contains read info
        print("File read and stored successfully")
        return content           # Return read info

# Read file by line function, reads one line of file with fileName
def readByLine(fileName):
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
    try:                        # Creates a file with exception handling
        f = open(fileName, "x") # Open file in X mode, opens file in write mode but throws
        registerFile(fileName)
        f.close()               # FileExistsError if file name already exists
    except FileExistsError:     # Throw excpetion
        print("File already exists.")

# Write to file function, takes in fileName and input arguments
def writeToFile(input, fileName):
    with open(fileName, 'w') as file:     # Open file in Write mode
        file.write(input)                 # Write input to file
    registerFile(fileName)

def writeByLine(input, fileName):
    with open(fileName, 'w') as file:
        for line in input:
            file.write(line)

def registerFile(fileName):
    try:
        readable_files = readByLine("readable_files.txt")[:-1]  # a text file containing all readable files
    except FileNotFoundError:
        readable_files = []
    readable_files.append(f"{fileName}\n")
    writeByLine(readable_files, "readable_files.txt")

def deleteFile(fileName):
    old_readable_files = readByLine("readable_files.txt")
    new_readable_files = []
    for file in old_readable_files:
        if file.strip("\n") != fileName:
            new_readable_files.append(file)
    writeByLine(new_readable_files, "readable_files.txt")

def isReadable(fileName):
    if fileName != "readable_files.txt" and f"{fileName}\n" not in readByLine("readable_files.txt"):
        raise FileNotFoundError(f"{fileName} does not exist for purposes of this function.")

def main():
    for i in range(10):
        file = f"jank{i}.txt"
        deleteFile(file)
        try:
            print(readFromFile(file))
        except FileNotFoundError as e:
            print(i)

if __name__ == '__main__':
    main()
