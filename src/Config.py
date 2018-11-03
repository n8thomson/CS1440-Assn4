import sys


class Config():




    def createConfigDict(self):
        dict = {}

        file = open("data/" + sys.argv[1])
        print(file.read())



        for line in file:
            dict[line.split(":")[0]] = print(line.split(":")[1].strip())

        return dict


