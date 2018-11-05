import ImagePainter

def mandelbrot(c, iterations):
    z = complex(0, 0)
    return ImagePainter.theLoop(z, c, iterations)