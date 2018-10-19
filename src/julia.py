#!/usr/bin/python3

## Julia Set Visualizer

import sys
from tkinter import Tk, Canvas, PhotoImage, mainloop


def getColorFromGradient(z):
    """Return the color of the current pixel within the Julia set"""
    # TODO: I understand that you can get more 'interesting' images when you
    #       use a different value for c.  Maybe I can encode this into the
    #       image configuration dictionary down below...
    c = complex(-1, 0) # c0
    
    # TODO: I feel bad about all of the global variables I'm using.
    #       There must be a better way...
    global grad
    
    # TODO: Make it easier to support more colors in the gradient
    for i in range(78):
        z = z * z + c # Get z1, z2, ...
        if abs(z) > 2:
            return grad[i] # The sequence is unbounded
    # TODO: Support more than 78 iterations as the bailout condition
    return grad[77] # Indicate a bounded sequence



def makePicture(f, imagename):
    """Paint a Fractal image into the TKinter PhotoImage canvas.  Assumes the
    image is 1024x1024 pixels.
    This function displays a really handy status bar so you can see how far
    along in the process the program is."""
    
    global grad
    global img
    
    # Figure out how the boundaries of the PhotoImage relate to coordinates on
    # the imaginary plane.
    minimum = ( (f['centerX'] - (f['axisLength'] / 2.0)), 
            (f['centerY'] - (f['axisLength'] / 2.0)))

    maximum = ( (f['centerX'] + (f['axisLength'] / 2.0)),
            (f['centerY'] + (f['axisLength'] / 2.0)))

    # At this scale, how much length and height on the imaginary plane does one
    # pixel take?
    size = abs(maximum[0] - minimum[0]) / 1024
    
    fraction = int(1024 / 64)
    for c in range(1024):
        if c % fraction == 0:
            # Update the status bar each time we complete 1/64th of the rows
            dots = c // fraction
            percent = c / 1024
            print(f"{imagename} (1024x1024) {'=' * dots}{'_' * (64 - dots)} {percent:.0%}", end='\r', file=sys.stderr)
        for r in range(1024):
            x = minimum[0] + c * size
            y = minimum[1] + r * size
            color = getColorFromGradient(complex(x, y))
            img.put(color, (c, r))
    print(f"{imagename} ({1024}x{1024}) ================================================================ 100%", file=sys.stderr)
    
    # Display the image on the screen
    # TODO: Sometimes I wonder whether some of my functions are trying to do
    #       too many different things
    canvas = Canvas(window, width=1024, height=1024, bg=grad[0])
    canvas.pack()
    canvas.create_image((512, 512), image=img, state="normal")
            

# TODO: This color gradient contains 78 color steps.  It would be nice if I
# could add more or different colors to this list, but it's so much work to
# calculate all of the in-between shades!
grad = ['#ffffff', '#ff00ff', '#ff00f1', '#ff00e4', '#ff00d6', '#ff00c9',
        '#ff00bb', '#ff00ae', '#ff00a1', '#ff0093', '#ff0086', '#ff0078',
        '#ff006b', '#ff005d', '#ff0050', '#ff0043', '#ff0035', '#ff0028',
        '#ff001a', '#ff000d', '#ff0000', '#ff0d00', '#ff1a00', '#ff2800',
        '#ff3500', '#ff4300', '#ff5000', '#ff5d00', '#ff6b00', '#ff7800',
        '#ff8600', '#ff9300', '#ffa100', '#ffae00', '#ffbb00', '#ffc900',
        '#ffd600', '#ffe400', '#fff100', '#ffff00', '#f1ff00', '#e4ff00',
        '#d6ff00', '#c9ff00', '#bbff00', '#aeff00', '#a1ff00', '#93ff00',
        '#86ff00', '#78ff00', '#6bff00', '#5dff00', '#50ff00', '#43ff00',
        '#35ff00', '#28ff00', '#1aff00', '#0dff00', '#00ff00', '#00ff0d',
        '#00ff1a', '#00ff28', '#00ff35', '#00ff43', '#00ff50', '#00ff5d',
        '#00ff6b', '#00ff78', '#00ff86', '#00ff93', '#00ffa1', '#00ffae',
        '#00ffbb', '#00ffc9', '#00ffd6', '#00ffe4', '#00fff1', '#00ffff']


# These are the different views of the Julia set you can make with this
# program.
#
# For convenience I have placed these into a dictionary so you may easily
# switch between them by entering the name of the image you want to generate
# into the variable 'image'.
#
# Add more parameters to this dictionary to create new Julia pictures!
#
# Get some ideas from http://bl.ocks.org/syntagmatic/3736720
#
# TODO: write a small helper program to convert the websites'
#       (minX, minY), (maxX, maxY) coordinates into my
#       (centerX, centerY) + axisLength scheme
#
# TODO: It would be nice to be able to visualize different parts of the
#       Julia set without needing to hard-code params into this program.
pictures = {
        'fulljulia': {
            'centerX':     0.0,
            'centerY':     0.0,
            'axisLength':  4.0,
            },

        'hourglass': {
            'centerX':     0.618,
            'centerY':     0.00,
            'axisLength':  0.017148277367054,
        },

        'lakes': {
            'centerX': -0.339230468501458,
            'centerY': 0.417970758224314,
            'axisLength': 0.164938488846612,
            }
        }

i = 'hourglass'


# Set up the GUI so that we can paint the fractal image on the screen
# and into a PNG image.
window = Tk()

# TODO: Make the program output images in different sizes without needing to
#       rewrite many lines of code
img = PhotoImage(width=1024, height=1024)
makePicture(pictures[i], i)

# Save the picture to a GIF
# TODO: I have heard that you can create pictures in other formats, such as PNG
#       and PPM.  I wonder how I do that?
img.write(i + ".gif")
print(f"Wrote picture {i}.gif")
mainloop()
