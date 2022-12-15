from turtle import *

### BEGIN HELPER FUNCTIONS ###

def initializeTurtle():
    """Setups up the window and initializes the turtle
    to be at the base of the main trunk facing north"""
    setup(600, 600) # Create a turtle window
    reset() # Clear any existing turtle drawings
            # and reset turtle position & heading.
    pensize(1) # Choose a pen thickness
    speed(0) # Set the speed; 0=fastest, 1=slowest, 6=normal
    # By default turtle starts at (0,0): center of the screen
    # and by default faces east
    # set turtle to be roughly off center
    up()
    goto(-100,-200)
    # have it face north
    left(90)
    down()


def testShrub(trunkLength, angle, shrinkFactor, minLength):
    """Initializes turtle, calls shrub and prints returned tuples & saves figure"""
    initializeTurtle()
    numBranches, totLength = shrub(trunkLength, angle, shrinkFactor, minLength)
    print('shrub({}, {}, {}, {}) -> ({}, {})'.format(trunkLength, angle, shrinkFactor,
                              minLength, numBranches, totLength))
    getscreen().getcanvas().postscript(file="shrub({},{},{},{}).ps".format
                            (trunkLength, angle, shrinkFactor, minLength))

### END HELPER FUNCTIONS ###

#*******************************************************************************
# Task 4: Fruitful Recursive shrub function
#*******************************************************************************

def shrub(trunkLength, angle, shrinkFactor, minLength):
    """
    Draws a shrub as specified in Lab 9 Task 4.
    Returns a pair (a 2-tuple) consisting of
      (1) the total number of branches (including the trunk) and
      (2) the total length of the branches (including the trunk)
    of the shrub.
    Assume that the turtle is positioned at the base of the main
    trunk facing north before this function is called.
    """
    numLines = 0
    lineLength = 0
    #base case -
    if trunkLength <= minLength:
        return (0,0)
    else:
        #draw trunk
        forward(trunkLength)
        #turn right by angle
        right(angle)
        #call shrub and return a tuple everytime its called that returns
        #number of branches and length of branches
        righttuple  = shrub(trunkLength*shrinkFactor, angle, shrinkFactor, minLength)
        #reorient turtle and draw left side of tree
        left(2*angle)
        lefttuple =shrub(trunkLength*(shrinkFactor**2), angle, shrinkFactor, minLength)
        #reorient turtle
        right(angle)
        #lift pen to not draw on return to starting point
        up()
        #return turtle to starting point
        backward(trunkLength)
        down()

    #add 1 to numLines and trunkLength to lineLength to account for trunk
    numLines += righttuple[0] + lefttuple[0] + 1
    lineLength += righttuple[1] + lefttuple[1] + trunkLength

    #return tuple that returns total number of lines and length for tree
    return (numLines, lineLength)


#************************************************************************************
# Testing code given in if __name__ == '__main__' block below
#************************************************************************************

if __name__=='__main__':
    """Testing code"""
    # Uncomment these (one at a time) to test your recursiveSqCount function
    pass
    #testShrub(100, 15, 0.8, 60) # should print (4, 308.0)
    #testShrub(100, 15, 0.8, 50) # should print (7, 461.6)
    #testShrub(100, 15, 0.8, 40) # should print (12, 666.4000000000001)
    #testShrub(100, 30, 0.82, 40) # should print (12, 707.95128)
    #testShrub(200, 90, 0.75, 40) # should print (20, 1524.21875)
    testShrub(100, 15, 0.8, 10) # should print (232, 3973.9861913600025)
    #testShrub(100, 30, 0.82, 10) # should print (376, 6386.440567704483)
    #testShrub(200, 90, 0.75, 10) # should print (232, 5056.675148010254)
    # uncomment line below if you don't want turtle screen to close automatically
    exitonclick()
