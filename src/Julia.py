from Fractal import Fractal


class Julia(Fractal):
    def __init__(self):
        pass

    def count(self, z, iterations):
        c = complex(-1, 0)
        for i in range(iterations):
            z = z * z + c
            if abs(z) > 2:
                return i
        return (iterations - 1)
