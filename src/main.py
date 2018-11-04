from tkinter import Tk, Canvas, PhotoImage, mainloop
import Config
import ImagePainter

theDictionary = Config.createConfigDict()

pixels = theDictionary['pixels']

window = Tk()
img = PhotoImage(width=pixels, height=pixels)

ImagePainter(theDictionary, '''ADD GRADIENT''', img)