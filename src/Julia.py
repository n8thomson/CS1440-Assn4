import ImagePainter


def julia(z, iterations, cReal, cImag):
    c = complex(cReal, cImag)
    return ImagePainter.theLoop(z, c, iterations)
