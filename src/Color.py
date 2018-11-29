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
            self.r = r

    def setGreen(self, g):
        """Setter for Green color channel which ensures value is in-range"""
        if g < 0:
            self.g = 0
        elif g > 255:
            self.g = 255
        else:
            self.g = g

    def setBlue(self, b):
        """Setter for Blue color channel which ensures value is in-range"""
        if b < 0:
            self.b = 0
        elif b > 255:
            self.b = 255
        else:
            self.b = b

    def __str__(self):
        return f"#{self.r:02x}{self.g:02x}{self.b:02x}"

    def __repr__(self):
        return self.__str__()


# Test code to demonstrate how a Color may be used
if __name__ == '__main__':
    red = Color(255, 0, 0)
    print(f"red is {red}")

    green = Color(0, 255, 0)
    print(f"green is {green}")

    blue = Color(0, 0, 255)
    print(f"blue is {blue}")

    firebrick = Color(178, 34, 34)
    print(f"firebrick is {firebrick}")

    aliceblue = Color(240, 248, 255)
    print(f"aliceblue is {aliceblue}")

    deepskyblue = Color(0, 191, 255)
    print(f"deepskyblue is {deepskyblue}")

    seashell2 = Color(238, 229, 222)
    print(f"seashell2 is {seashell2}")

    default = Color()
    print(f"The default color is {default}")

    default.setRed(299)
    default.setGreen(377)
    default.setBlue(-12)
    print(f"After trying to modify `default' in invalid ways we get {default}")

    invalid = Color(299, 377, -12)
    print(f"Invalid RGB values in `Color(299, 377, -12)' are clamped to: {invalid}")
