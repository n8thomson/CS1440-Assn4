from Christmas import Christmas
from Grayscale import Grayscale

def makeGradient(args):
    if len(args) < 3:
        print("GradientFactory: Creating default color gradient")
        return Grayscale()
    else:
        colorScheme = args[2].lower()
    if colorScheme == 'christmas':
        print("GradientFactory: Creating " + args[2] + " color gradient")
        return Christmas()
    if colorScheme == 'grayscale':
        print("GradientFactory: Creating " + args[2] + " color gradient")
        return Grayscale()
    print("GradientFactory: Unknown gradient '" + args[2] + "'; creating default color gradient")
    return Grayscale()
