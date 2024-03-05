"""three functions: write, append, and read a file

with open is the Context Manager pattern
- allows you to create and read files


"""
# the argument is passed to the function and assigned as the value to the parameter

def writeToFile(filename, txt):
    with open(filename, 'w') as write_file:
        write_file.write(txt)

def appendToFile(filename, txt):
    with open(filename, 'a') as append_file:
        append_file.write(txt)

def readFromFile(filename):
    with open(filename, 'r') as read_file:
        return read_file.read()



writeToFile('greet.txt', 'Hello!\n')
appendToFile('greet.txt', 'Goodbye!\n')
readFromFile('greet.txt')
assert readFromFile('greet.txt') == 'Hello!\nGoodbye!\n'
