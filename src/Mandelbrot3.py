from Fractal import Fractal

class Mandelbrot3(Fractal):
    def __init__(self):
        pass


    def count(self, c, iterations):
        z = complex(0, 0)
        for i in range(iterations):
            z = z * z * z + c
            if abs(z) > 2:
                return i
        return (iterations - 1)
