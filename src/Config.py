import sys


def createConfigDict(self):
    d = {}

    file = open("data/" + sys.argv[1])
    print(file.read())

    for line in file:
        d[line.split(":")[0]] = print(line.split(":")[1].strip())

    return d
