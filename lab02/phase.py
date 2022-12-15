"""
Computing the Age of the Moon
=============================

phase.py is a Python module integrating Conway's algorithm to compute the age of
moon, as a value between 0 and 29 that represents the number of days since the
last new moon.

The age of the moon can be used to determine which of 8 moon phases was or will
be observed on any given day. When the age is zero, the moon is new and when the
age is 15, the moon is full.

"""
__all__ = [ "moonAge", "age2Str" ]

def moonAge(month, day, year):

    """Compute the age of the moon based on a month, day, and year.
       N.B. Order of parameters is important.

       :param int month: month specified as a value between 1 and 12
       :param int year: year in the range 1900 to 2099
       :param int day: day specified as a value between 1 and 31

       >>> moonAge(7,20,1969)
       6
       >>> moonAge(9,28,1967)
       24
    """
    #The algorithm involves keeping a running sum, initialize the sum.
    rsum = month + day + 30
    if (year // 1000) == 2:
        rsum = rsum - 8
    else :
        rsum = rsum - 4

    #Compute the value of the year within the century, yy.
    yy = abs(year) % 100

    #Compute the distance of yy to the closest multiple of 19
    dist = yy % 19
    if dist > 9 :
        dist = dist - 19
    else :
        dist = dist

    #Compute final dist by inserting a ten's digit to dist equivalent to the
    #remainder when dist is divided by 3
    tens = (abs(dist) % 3)*10
    if dist >= 0:
        dist = tens + dist
    else:
        dist = -1 * (tens + abs(dist))

    #Compute the age of the moon
    moonAge = (dist + rsum) % 30
    return (moonAge)

def age2Str(age):
    """Convert a moon age in days to a textual description of the moon phase.

        :param int age: age of the moon specified as a value between 0 and 29

        >>>age2Str(0)
        new
        >>>age2Str(15)
        full
    """
    #textual descriptions for each moonAge
    if age <2 or age>28:
       phase= "new moon"
    elif age <14:
        if age>8:
            phase="waxing gibbous moon"
        elif age<7:
            phase="waxing crescent moon"
        else:
            phase="first quarter moon"
    elif age <22:
        if age>16:
            phase="waning gibbous"
        else:
            phase="full moon"
    else:
        if age>23:
            phase="waning crescent moon"
        else:
            phase="third quarter moon"
    return phase

def main():
    """A method that prompts for a date and prints the moon's age and phase."""
    month = int(input("Month? "))
    day = int(input("Day? "))
    year = int(input("Year (yyyy)? "))
    age = moonAge(month,day,year)
    phase = age2Str(age)
    print("On {}/{}/{}, the moon's age is {}, a {}.".format(month, day, year,
    age, phase))

if __name__ == "__main__":
    # The following code is executed when we execute this file as a script:
    main()
