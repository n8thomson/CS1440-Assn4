
from Mandelbrot import Mandelbrot
from Julia import Julia
from Mandelbrot3 import Mandelbrot3

def makeFractal(cfg):

    fracType = cfg['type'].lower()


    if fracType == 'mandelbrot':
        return Mandelbrot()

    if fracType == 'julia':
        return Julia()

    if fracType == 'mandelbrot3':
        return Mandelbrot3()
