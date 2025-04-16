# Levi Pitts
# CSC 450
# Devon Simmonds
# defines functions for reading from and writing to files

# Read file function, reads entire file with fileName
def readFromFile(fileName):
    # Open file in read mode
    with open(fileName) as file:
        # Set variable that contains read info
        content = file.read()
        print("File read and stored successfully")
        # Return read info
        return content

# Read file by line function, reads one line of file with fileName
def readByLine(fileName):
    # Open file in read mode
    with open(fileName) as file:
        # Read one line of file, return line
        line = file.readline()
        return line

# Create file function with desired file name
def newFile(fileName):
    # Creates a file with exception handling
    try:
        # Open file in X mode, opens file in write mode but throws
        # FileExistsError if file name already exists
        f = open(fileName, "x")
        f.close()
    # Throw excpetion
    except FileExistsError:
        print("File already exists.")

# Write to file function, takes in fileName and input arguments
def writeToFile(input, fileName):
    # Open file in Write mode
    with open(fileName, 'w') as file:
        # Write input to file
        file.write(input)
