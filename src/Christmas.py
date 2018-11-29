from Gradient import Gradient
from Color import Color


class Christmas(Gradient):
    def __init__(self):
        pass

    def getGradient(self, iterations):
        return self.linerlyInterpolate(iterations,  Color(255, 0, 0),  Color(0, 255, 0))