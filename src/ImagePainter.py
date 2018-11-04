from tkinter import Tk, Canvas, PhotoImage, mainloop
import sys
import MyMandelbrot
import MyJulia


def paint(fractal, gradient, img):

    type = fractal['type']
    pixels = fractal['pixels']
    centerX = fractal['centerX']
    centerY = fractal['centerY']
    axisLength = fractal['axisLength']
    iterations = fractal['iterations']

    if type = "Mandelbrot":
        MyMandelbrot.mandelbrot('''INSERT''')
        else:
        MyJulia.julia('''INSERT''', fractal['cReal'], fractal['cImag'])


    minx = centerX - (axisLength / 2.0)
    maxx = centerX + (axisLength / 2.0)
    miny = centerY - (axisLength / 2.0)
    maxy = centerY + (axisLength / 2.0)

    pixelsize = abs(maxx - minx) / pixels

    portion = int(pixels / 64)

    for col in range(pixels):
        if col % portion == 0:
            # Update the status bar each time we complete 1/64th of the rows
            pips = col // portion
            pct = col / pixels
            print(f"{imagename} ((pixels)x(pixels)) {'=' * pips}{'_' * (64 - pips)} {pct:.0%}",
                  end='\r', file=sys.stderr)
        for row in range(pixels):
            x = minx + col * pixelsize
            y = miny + row * pixelsize
            color = colorOfThePixel(complex(x, y), gradient)
            img.put(color, (col, row))
    print(
        f"{imagename} ({pixels}x{pixels}) ================================================================ 100%",
        file=sys.stderr)

    canvas = Canvas(Tk(), width=pixels, height=pixels, bg=gradient[0])
    canvas.pack()
    canvas.create_image((pixels / 2, pixels / 2),
                        image=img, state="normal")

    def theLoop(z, c):
        for i in range(iterations):
            z = z * z + c
            if abs(z) > 2:
                return gradient[i]
        return gradient[iterations - 1]