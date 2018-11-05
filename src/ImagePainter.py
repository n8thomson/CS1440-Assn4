from tkinter import Tk, Canvas, PhotoImage, mainloop
import sys
import Mandelbrot
import Julia
import Gradient
import Color



def paint(fractal, img, window, imagename, r1, g1, b1, r2, g2, b2):


    type = fractal['type'].lower()
    pixels = int(fractal['pixels'])
    centerX = float(fractal['centerx'])
    centerY = float(fractal['centery'])
    axisLength = float(fractal['axislength'])
    iterations = int(fractal['iterations'])

    startColor = Color.Color(r1, g1, b1)
    stopColor = Color.Color(r2, g2, b2)

    gradient = Gradient.Gradient().linerlyInterpolate(iterations, startColor, stopColor)


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
            if type == "mandelbrot":
                color = gradient[Mandelbrot.mandelbrot(complex(x, y), iterations)]
            if type == "julia":
                color = gradient[Julia.julia(complex(x, y), iterations, int(fractal['creal']), int(fractal['cimag']))]

            img.put(color, (col, row))
    print(
        f"{imagename} ({pixels}x{pixels}) ================================================================ 100%",
        file=sys.stderr)

    canvas = Canvas(window, width=pixels, height=pixels, bg=gradient[0])
    canvas.pack()
    canvas.create_image((pixels / 2, pixels / 2),
                        image=img, state="normal")




def theLoop(z, c, iterations):
    for i in range(iterations):
        z = z * z + c
        if abs(z) > 2:
            return i
    return (iterations - 1)
