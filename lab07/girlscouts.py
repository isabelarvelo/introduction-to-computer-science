#******************************************************************************
# Task 1: totalCookieOrder (fruitful)
# Calculates the total number of boxes of cookies for a Girl Scout
# who only sells Tagalongs
#******************************************************************************

def totalCookieOrder(orders):
    """
    returns thte total number of boxes of cookies represented by the inputed
    orders list
    >>> totalCookieOrder([])
    0
    >>> totalCookieOrder([1, 3, 2])
    6
    >>> totalCookieOrder([4, [5, 6], 10, [1, 1, 1]])
    28
    """
    #base case - There are no orders so the total number of boxes is 0.
    if not orders:
        return 0
    #look at first element of list
    first = orders.pop()
    #if first element is a list- call the function recursively to count number
    #of boxes within that list and add it to rest of orders
    if isinstance(first,list):
        return totalCookieOrder(first) + totalCookieOrder(orders)
    #if element is not a list add first element of list to the to sum of the rest
    else:
        return first + totalCookieOrder(orders)

if __name__ == "__main__":
    from doctest import testmod
    testmod()
