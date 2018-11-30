from Color import Color

class Gradient():
    def __init__(self):
        raise NotImplementedError("Don't instantiate a Gradient!  Instantiate a subclass of Gradient!!!")



    def linerlyInterpolate(self, steps, start, stop):
        dRed = (stop.r - start.r) / (steps - 1)
        dGrn = (stop.g - start.g) / (steps - 1)
        dBlu = (stop.b - start.b) / (steps - 1)
        return list(map(lambda n: Color(int(n * dRed) + start.r, int(n * dGrn) + start.g, int(n * dBlu) + start.b) , range(steps)))

    def getGradient(self, iterations):
        pass




