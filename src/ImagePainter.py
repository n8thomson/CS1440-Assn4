from tkinter import Tk, Canvas, PhotoImage, mainloop
import sys



def paint(cfg, img, window, imagename, fractalObject, gradient):


    type = cfg['type']
    pixels = int(cfg['pixels'])
    centerX = float(cfg['centerx'])
    centerY = float(cfg['centery'])
    axisLength = float(cfg['axislength'])
    iterations = int(cfg['iterations'])




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
            print(f"{imagename} ({pixels}x{pixels}) {'=' * pips}{'_' * (64 - pips)} {pct:.0%}", end='\r', file=sys.stderr)
        for row in range(pixels):
            x = minx + col * pixelsize
            y = miny + row * pixelsize
            color = gradient[fractalObject.count(complex(x, y), iterations)]
            img.put(color, (col, row))
    print(f"{imagename} ({pixels}x{pixels}) ================================================================ 100%", file=sys.stderr)

    canvas = Canvas(window, width=pixels, height=pixels, bg=gradient[0])
    canvas.pack()
    canvas.create_image((pixels / 2, pixels / 2), image=img, state="normal")





