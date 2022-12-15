from turtle import *
from math import sqrt

#*****************************************************************************
#  Global variables:  Some HEX colors
#*****************************************************************************
#Questions: turtle orientation not same for all, position on screen

purple = '#8E44AD'
gold = '#F4D03F'
red = '#f01616'
green = '#09d646'
gray = '#8e918f'
blue = '#4287f5'
orange = '#fa922a'

### BEGIN HELPER FUNCTIONS ###
def drawBar(width, length, color):
    """Draws a single rectangle of side length size and given color
    assuming turtle is initially at one of its endpoints.
    Turtle starts traveling along its width and ends at the same point,
    having drawn its length."""
    down()
    pen(fillcolor = color)
    begin_fill()
    forward(width)
    left(90)
    forward(length)
    left(90)
    forward(width)
    left(90)
    forward(length)
    end_fill()
    up()

def initializeTurtle(w, l):
    """Setups up the window and initializes the turtle
    to be at the bottom left corner of the pattern
    facing east (which is the default direction)."""
    padding = w  # increase if patterns gets cut off
    # Create a turtle window
    setup(width = 2 * (l + w), height = 2 * (l + w) )
    reset() # Clear any existing turtle drawings
            # and reset turtle position & heading.
    pensize(1) # Choose a pen thickness
    speed(0) # Set the speed; 0=fastest, 1=slowest, 6=normal
    # By default turtle starts at (0,0): center of the screen
    # and by default faces east
    # Put turtle in bottom left corner of the quilt
    up()
    goto(l/2,-l/2) #start at lower lefthand corner
    down()

def testDrawVortex(width, length, currColor):
    """Initializes turtle, calls drawVortex and saves figure"""
    # initialize turtle
    initializeTurtle(width, length)
    # call drawVortex
    drawVortex(width, length, currColor)
    # save the figure
    getscreen().getcanvas().postscript(file="drawVortex({}, {}, {}).ps".format(width, length, currColor))


### END HELPER FUNCTIONS ###

#*****************************************************************************
# Task 3: Draw recursive vortex (Non-fruitful recursion)
#*****************************************************************************
def drawVortex(width, length, colorList):
    """Draws a colored vortex as described in Lab 9 Task 3.
    """
    width = int(width)
    length = int(length)

    color = colorList[0]

#base case: need to be able to draw all four bars without gaps so stop drawing
#width is greater than length

    if  length >= width:
        #drawing outer bars of vortex
        drawBar(width, length, color)
        backward(width)
        right(90)
        drawBar(length, width, color)
        left(90)
        forward(length-width)
        right(90)
        drawBar(length, width, color)
        left(90)
        forward(length - width)
        right(90)
        drawBar(length, width, color)
        forward(length - 2*width)
        #add first color to end of list
        colorList.append(color)
        #pop off the first color of the list so that next layer is the next color
        #in the list
        colorList.pop(0)
        #for each layer of the vortex the width stays the same and length
        #decreases by double the width to fit inside outer bars
        #call Vortex recursively
        drawVortex(width,length -2*width,colorList)

        #Duane said that the turtle does not need to end up in the same spot as
        #it does in the figures in the lab handout

        #Extra thinking: The pattern will be filled in if there exists a value x
        #such that width + 2x(width) = length. If (2* width) does not divide
        #evenly into length -width then the pattern will have a hole in the
        #middle.

        #please run tests to look at my final graphics because I was unable
        #to push updated versions to github

#*****************************************************************************
# Testing code given in if __name__ == '__main__' block below
#*****************************************************************************

if __name__=='__main__':
    """Testing code"""

    # Uncomment these (one at a time) to test your drawVortex function
    #testDrawVortex(50, 100, [purple])
    #testDrawVortex(50, 550, [orange, gray])
    #testDrawVortex(50, 500, [red, blue, green])
    #testDrawVortex(5, 500, [red, orange, gold, green, blue, purple, gray])
    exitonclick()
