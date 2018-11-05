import sys


def createConfigDict():
    d = {}

    fileName = sys.argv[1]
    file = open(fileName)




    for line in file:
        if ":" in line :
            d[line.split(":")[0].lower()] = line.split(":")[1].strip()

    return d

def getSimpleFileName():

    return str(sys.argv[1].split("/")[1]).split(".")[0]
