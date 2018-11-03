from tkinter import Tk, Canvas, PhotoImage, mainloop


class ImagePainter():
    def __init__(self):

        self.__m_fractal = Config.createConfigDict()
        self.__m_type = self.__m_fractal['type']
        self.__m_pixels = self.__m_fractal['pixels']
        self.__m_centerX = self.__m_fractal['centerX']
        self.__m_centerY = self.__m_fractal['centerY']
        self.__m_axisLength = self.__m_fractal['axisLength']

        minx = self.__m_centerX - (self.__m_fractal['axisLength'] / 2.0)
        maxx = self.__m_fractal['centerX'] + (self.__m_fractal['axisLength'] / 2.0)
        miny = self.__m_fractal['centerY'] - (self.__m_fractal['axisLength'] / 2.0)
        maxy = self.__m_fractal['centerY'] + (self.__m_fractal['axisLength'] / 2.0)

        pixelsize = abs(maxx - minx) / self.__m_fractal['pixels']









