class Color():
    """A class to represent RGB colors

    Use the setters to ensure color channel values stay within the accepted
    range of 0..255
                                                                            
    To-string functions express colors in PhotoImage-compatible hexidecimal
    #RRGGBB notation.
    """

    def __init__(self, r=0, g=0, b=0):
        self.setRed(r)
        self.setGreen(g)
        self.setBlue(b)


    def setRed(self, r):
        """Setter for Red color channel which ensures value is in-range"""
        if r < 0:
            self.r = 0
        elif r > 255:
            self.r = 255
        else:
            self.r = int(r)


    def setGreen(self, g):
        """Setter for Green color channel which ensures value is in-range"""
        if g < 0:
            self.g = 0
        elif g > 255:
            self.g = 255
        else:
            self.g = int(g)


    def setBlue(self, b):
        """Setter for Blue color channel which ensures value is in-range"""
        if b < 0:
            self.b = 0
        elif b > 255:
            self.b = 255
        else:
            self.b = int(b)

    def __str__(self):
        return f"#{self.r:02x}{self.g:02x}{self.b:02x}"
        #return f"Color({self.r}, {self.g}, {self.b})"


    def __repr__(self):
        return self.__str__()


def gradient(start, stop, steps):
    dRed = (stop.r - start.r) / (steps - 1)
    dGrn = (stop.g - start.g) / (steps - 1)
    dBlu = (stop.b - start.b) / (steps - 1)
    return list(
        map(lambda n: Color((n * dRed) + start.r, (n * dGrn) + start.g, (n * dBlu) + start.b) , range(steps)))


# Test code to demonstrate how a Color may be used
if __name__ == '__main__':
    red   = Color(255, 0, 0)
    print(f"red is {red}")

    green = Color(0, 255, 0)
    print(f"green is {green}")

    blue  = Color(0, 0, 255)
    print(f"blue is {blue}")

    print(gradient(red, green, 512))
