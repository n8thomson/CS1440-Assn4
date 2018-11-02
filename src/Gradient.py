from Color import Color

class Gradient():
    def __init__(self):
        raise NotImplementedError("Don't instantiate a Gradient!  Instantiate a subclass of Gradient!!!")

    def getColor(self, n):
        return self.colors[n - 1]

    def getFirstColor(self):
        return self.colors[0]

    def getLastColor(self):
        return self.colors[-1]

    def getNumColors(self):
        return len(self.colors)

    def linerlyInterpolate(self, steps, start, stop):
        dRed = (stop.r - start.r) / (steps - 1)
        dGrn = (stop.g - start.g) / (steps - 1)
        dBlu = (stop.b - start.b) / (steps - 1)
        return list(
            map(lambda n: Color((n * dRed) + start.r, (n * dGrn) + start.g, (n * dBlu) + start.b) , range(steps)))

    def __str__(self):
        return f"This is a gradient of {self.getNumColors()} colors: {self.colors}"


if __name__  != '__main__':
    print(f"__name__ is {__name__}")
