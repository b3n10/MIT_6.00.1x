'''
Grader
10/10 points (ungraded)
A regular polygon has n number of sides. Each side has length s.

The area of a regular polygon is: 0.25 * n * s**2 / tan(pi/n)
The perimeter of a polygon is: length of the boundary of the polygon
Write a function called polysum that takes 2 arguments, n and s. This function should sum the area and square of the perimeter of the regular polygon. The function returns the sum, rounded to 4 decimal places.

Hint: What to import?
Which library should you be importing at the beginning of your code in order to call the tan function and to get the pi constant?
This is an optional exercise, but great for extra practice!
'''
from math import *

def polysum(n, s):
    area = ( (0.25 * n) * s**2 ) / (tan(pi/n))
    perimeter = n * s

    return round( area + (perimeter**2), 4 )

print( polysum(95, 10) )
