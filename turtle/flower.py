import turtle
from polygon import arc
bob = turtle.Turtle()

def petal(t, r, angle): 
    """Draw petals with given radius and angle
    t: Turtle
    r: raduus 
    angle: angle subtended by the arc 
    """
    for i in range(2):
        arc(t, r, angle)
        t.lt(180-angle)

def flower(t, r, angle, n):
    """Draw flower with given radius, angle and number of petals
    t: Turtle
    r: radius
    angle: angle subtended by the arc of petal
    n: number of petals
    """
    for i in range(n):
        petal(t, r, angle)
        t.lt(360.0 / n)

def move(t, length):
    """Move Turtle (t) forward (length) units without leaving a trail.
    Leaves the pen down.
    """
    t.pu()
    t.fd(length)
    t.pd()

move(bob, -100)
flower(bob, 60.0, 60.0, 7)

move(bob, 100)
flower(bob, 40.0, 80.0, 10)

move(bob, 100)
flower(bob, 140.0, 20.0, 20)

turtle.mainloop() #tells the window to wait for the user to do something
