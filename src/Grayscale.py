from Gradient import Gradient
from Color import Color


class Grayscale(Gradient):
    def __init__(self):
        pass

    def getGradient(self, iterations):
        return self.linerlyInterpolate(iterations, Color(0, 0, 0), Color(255, 255, 255))
