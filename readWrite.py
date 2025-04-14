# Levi Pitts
# CSC 450
# defines functions for reading from and writing to files

def readFromFile(fileName):
    with open(fileName) as file:
        content = file.read()
        print("File read and stored successfully")
        return content

def newFile(fileName):
    try:
        f = open(fileName, "x")
        f.close()
    except FileExistsError:
        print("File already exists.")

def writeToFile(input, fileName):
    with open(fileName, 'w') as file:
        file.write(input)
