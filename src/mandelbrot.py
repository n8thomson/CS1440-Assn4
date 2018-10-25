#!/usr/bin/python3

## Mandelbrot Set Visualizer

import sys
from tkinter import Tk, Canvas, PhotoImage, mainloop


# TODO: Sometimes I wonder whether my functions really need to be given all of
#       the data I pass to them
def colorOfThePixel(c, gradient):
    """Return the color of the current pixel within the Mandelbrot set"""
    # TODO: Make a way to paint a Julia Set; after all, it's algorithm is similar
    #       to the Mandelbrot set
    z = complex(0, 0) # z0
    
    # TODO: Make it easier to support more colors in the gradient
    for i in range(100):
        z = z * z + c # Get z1, z2, ...
        if abs(z) > 2:
            return gradient[i] # The sequence is unbounded
    # TODO: Support more than 100 iterations as the bailout condition
    return gradient[99] # Indicate a bounded sequence



# TODO: Sometimes I wonder whether some of my functions are trying to do too
#       much
def paint(fractal, imagename):
    """Paint a Fractal image into the TKinter PhotoImage canvas.  Assumes the
    image is 640x640 pixels.
    This function displays a really handy status bar so you can see how far
    along in the process the program is."""
    
    # TODO: I feel bad about all of the global variables I'm using.
    #       There must be a better way...
    global gradient
    global img
    
    # Figure out how the boundaries of the PhotoImage relate to coordinates on
    # the imaginary plane.
    minx = fractal['centerX'] - (fractal['axisLength'] / 2.0)
    maxx = fractal['centerX'] + (fractal['axisLength'] / 2.0)
    miny = fractal['centerY'] - (fractal['axisLength'] / 2.0)
    maxy = fractal['centerY'] + (fractal['axisLength'] / 2.0)

    # At this scale, how much length and height on the imaginary plane does one
    # pixel take?
    pixelsize = abs(maxx - minx) / 640
    
    portion = int(640 / 64)
    for col in range(640):
        if col % portion == 0:
            # Update the status bar each time we complete 1/64th of the rows
            pips = col // portion
            pct = col / 640
            print(f"{imagename} (640x640) {'=' * pips}{'_' * (64 - pips)} {pct:.0%}", end='\r', file=sys.stderr)
        for row in range(640):
            x = minx + col * pixelsize
            y = miny + row * pixelsize
            color = colorOfThePixel(complex(x, y), gradient)
            img.put(color, (col, row))
    print(f"{imagename} ({640}x{640}) ================================================================ 100%", file=sys.stderr)
    
    # Display the image on the screen
    canvas = Canvas(window, width=640, height=640, bg=gradient[0])
    canvas.pack()
    canvas.create_image((320, 320), image=img, state="normal")
            

# This color gradient contains 100 color steps.  It would be nice if I could
# add more or different colors to this list, but it's so much work to calculate
# all of the in-between shades!  If you look real close, you can see where I
# sort of gave up on it!
gradient = ['#ffe4b5', '#f5ddb2', '#ecd6af', '#e3cfad', '#d9c8aa', '#d0c1a8',
        '#c7bba5', '#beb4a3', '#b4ada0', '#aba69e', '#a29f9b', '#999999',
        '#999999', '#91969b', '#89949d', '#8292a0', '#7a90a2', '#738ea5',
        '#6b8ca7', '#648aaa', '#5c88ac', '#5586af', '#4d84b1', '#4682b4',
        '#4682b4', '#568da3', '#679893', '#78a482', '#89af72', '#9aba62',
        '#aac651', '#bbd141', '#ccdc31', '#dde820', '#eef310', '#feff00',
        '#ffff00', '#f6eb03', '#eed807', '#e6c40b', '#deb10f', '#d69e13',
        '#cd8a16', '#c5771a', '#bd641e', '#b55022', '#ad3d26', '#a52a2a',
        '#a52a2a', '#992929', '#8d2828', '#812727', '#752727', '#692626',
        '#5d2525', '#512424', '#452424', '#392323', '#2d2222', '#222222',
        '#222222', '#363031', '#4a3e40', '#5e4d50', '#725b5f', '#86696e',
        '#9a787e', '#ae868d', '#c2949c', '#d6a3ac', '#eab1bb', '#ffc0cb',
        '#ffc0cb', '#f6b1ce', '#eda2d1', '#e594d5', '#dc85d8', '#d377db',
        '#cb68df', '#c25ae2', '#b94be5', '#b13de9', '#a82eec', '#a020f0',
        '#a020f0', '#9120e5', '#8220da', '#7420cf', '#6520c4', '#5720b9',
        '#4821ae', '#3a21a3', '#2b2198', '#1d218d', '#0e2182', '#002277',
        '#002277', '#002277', '#002277', '#002277']


# These are the different views of the Mandelbrot set you can make with this
# program.
#
# For convenience I have placed these into a dictionary so you may easily
# switch between them by entering the name of the image you want to generate
# into the variable 'image'.
#
# Add more parameters to this dictionary to create new Mandelbrot images!
#
# Get some ideas from https://atopon.org/mandel/
# or https://sciencedemos.org.uk/mandelbrot.php
#
# TODO: write a small helper program to convert the websites'
#       (minX, minY), (maxX, maxY) coordinates into my
#       (centerX, centerY) + axisLength scheme
#
# TODO: It would be nice to be able to visualize different parts of the
#       Mandelbrot set without needing to hard-code params into this program.
images = {
        'fullmandelbrot': {
            'centerX':     0.0,
            'centerY':     0.0,
            'axisLength':  4.0,
            },

        'spiral0': {
            'centerX':    -0.761335372924805,
            'centerY':     0.0835704803466797,
            'axisLength':  0.00497817993164062,
            },

        'spiral1': {
            'centerX':    -0.747,
            'centerY':     0.1075,
            'axisLength':  0.002,
            },

        'seahorse': {
            'centerX':    -0.745,
            'centerY':     0.105,
            'axisLength':  0.01,
            },

        'elephants': {
            'centerX':     0.30820836067024604,
            'centerY':     0.030620936230004017,
            'axisLength':  0.03,
            },

        'leaf': {
            'centerX':     -1.543577002,
            'centerY':     -0.000058690069,
            'axisLength':  0.000051248888,
            },
        }

image = 'spiral0'


# Set up the GUI so that we can paint the fractal image on the screen
# and into a PNG image.
window = Tk()
img = PhotoImage(width=640, height=640)
paint(images[image], image)

# Save the image as a PNG
# TODO: I have heard that you can create pictures in other formats, such as GIF
#       and PPM.  I wonder how I do that?
img.write(image + ".png")
print(f"Wrote image {image}.png")
mainloop()
