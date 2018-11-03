import sys

file = open("data/" + sys.argv[1])




for line in file:
    print(line.split(":")[1].strip())
