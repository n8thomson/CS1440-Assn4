from tkinter import Tk, PhotoImage, mainloop
import Config
import ImagePainter
import FractalFactory
import GradientFactory
import sys

if len(sys.argv) == 1:
    print("Please supply a fractal configuration file as the first argument")
    sys.exit(0)

filetype = input("Input file save type (.png, .gif, etc): ")


cfg = Config.createConfigDict()
imagename = Config.getSimpleFileName()

pixels = cfg['pixels']

window = Tk()
img = PhotoImage(width=pixels, height=pixels)

fractal = FractalFactory.makeFractal(cfg)
gradient = GradientFactory.makeGradient(sys.argv).getGradient(int(cfg['iterations']))



ImagePainter.paint(cfg, img, window, imagename, fractal, gradient)

img.write(imagename + filetype)
print(f"Wrote image {imagename}" + filetype)
mainloop()
