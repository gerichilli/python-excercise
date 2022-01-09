import math
# import turtle #Import turtle module
# bob = turtle.Turtle() #Creates a Turtle object, which we assign to a variable named bob
# print(bob) 

def square(t, length):
    """ Draw a square with sides of the given length 
    t: Turtle object
    length: the length on sides of the square that you want to draw
    """
    for i in range(4):
        t.fd(length)
        t.lt(90)

# square(bob, 50)

def polyline(t, length, n, angle):
    """ Draw a polyline that has n line segments
    t: Turtle object
    length: length of line segments
    n: Number of line segments
    angle: degrees between segments
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)

# polyline(bob, 40, 6, 60)

def polygon(t, length, n):
    """ Draw a polylgon that has n sides
    t: Turtle object
    length: length of sides
    n: Number of sides
    """
    angle = 360 / n
    polyline(t, length, n, angle)

# polygon(bob, 40, 6)

def arc(t, r, angle):
    """ Draw an arc with given radius and angle
    t: Turtle object
    r: radius
    angle: angle subtended by the arc, in degrees
    """
    arc_length = 2 * math.pi * r * abs(angle) / 360
    #n: Number of line segments to draw circle
    n = int(arc_length / 4) + 3
    #step_length: The length of one line segment
    step_length = arc_length / n
    #step_angle: degrees between segments
    step_angle = float(angle) / n

    t.lt(step_angle / 2)
    polyline(t, step_length, n, step_angle)
    t.lt(step_angle / 2)

# arc(bob, 400, 360)

def circle(t, r):
    """Draw a turtle with given radius
    t: Turtle object
    r: radius
    """
    arc(t, r, 360)

# turtle.mainloop() #tells the window to wait for the user to do something