from tkinter import Tk, PhotoImage, mainloop
import Config
import ImagePainter


r1 = int(input("Input red value for color 1 (0 - 255): "))
g1 = int(input("Input green value for color 1 (0 - 255): "))
b1 = int(input("Input blue value for color 1 (0 - 255): "))

r2 = int(input("Input red value for color 2 (0 - 255): "))
g2 = int(input("Input green value for color 2 (0 - 255): "))
b2 = int(input("Input blue value for color 2 (0 - 255): "))


filetype = input("Input file save type (.png, .gif, etc): ")


theDictionary = Config.createConfigDict()
imagename = Config.getSimpleFileName()


pixels = theDictionary['pixels']

window = Tk()
img = PhotoImage(width=pixels, height=pixels)

ImagePainter.paint(theDictionary, img, window, imagename, r1, g1, b1, r2, g2, b2)

img.write(imagename + filetype)
print(f"Wrote image {imagename}" + filetype)
mainloop()
