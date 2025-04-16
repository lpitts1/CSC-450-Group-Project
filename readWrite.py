# Levi Pitts
# CSC 450
# Devon Simmonds
# defines functions for reading from and writing to files

# Read file function, reads entire file with fileName
def readFromFile(fileName):
    with open(fileName) as file: # Open file in read mode
        content = file.read()    # Set variable that contains read info
        print("File read and stored successfully")
        return content           # Return read info

# Read file by line function, reads one line of file with fileName
def readByLine(fileName):
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
        f.close()               # FileExistsError if file name already exists
    except FileExistsError:     # Throw excpetion
        print("File already exists.")

# Write to file function, takes in fileName and input arguments
def writeToFile(input, fileName):
    with open(fileName, 'w') as file:     # Open file in Write mode
        file.write(input)                 # Write input to file
