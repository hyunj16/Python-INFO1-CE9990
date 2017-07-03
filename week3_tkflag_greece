"""
tkflag.py

Draw the United States flag in color on a tkinter Canvas widget.
"""

import tkinter              #in Python2, the t was uppercase
import math

stripeHeight = 40           #height of each stripe

#The root widget is the window that will contain everything we draw.
root = tkinter.Tk()
root.title("United States Flag")

#dimensions of entire flag, in pixels
height = 9 * stripeHeight  #9 stripes
width = int(height * 3/2) #Wikipedia says aspect ratio of flag is 3:2
root.geometry(str(width) + "x" + str(height))

#red/green/blue colors
skyBlue = "#0D5EAF"
white = "#FFFFFF"


def drawPixel(x, y, color):
    """
    Color the pixel at coordinates (x, y).
    """
    assert isinstance(x, int) and isinstance(y, int) and isinstance(color, str)
    canvas.create_rectangle(x, y, x + 1, y + 1, width = 0, fill = color)

#highlightthickness = 0 allows the canvas to occupy the entire root.
canvas = tkinter.Canvas(root, highlightthickness = 0, background = white)

y = 0
while y < height:

    x = 0
    while x < width:

        if x < 5 * stripeHeight and 2 * stripeHeight< y < 3 * stripeHeight:
            drawPixel(x, y, white)
        elif 2 * stripeHeight < x < 3 * stripeHeight and y < 5 * stripeHeight:
            drawPixel(x, y, white)
        elif y % (2 * stripeHeight) < stripeHeight:
            drawPixel(x, y, skyBlue)
        elif x < 5 * stripeHeight and y < 5 * stripeHeight:
            drawPixel(x, y, skyBlue)
                               
        x += 1
    y += 1

#Make the canvas visible by packing it into the root.
canvas.pack(expand = tkinter.YES, fill = "both")

#If the flag had buttons, checkboxes, etc.,
#the mainloop would let them respond to touches.
root.mainloop()
