import math
import turtle

def pie(t, r, angle):
    """ Draw a isosceles triangle with given length(r) of 2 sides that have
        the same length and the angle that created by these sides
    """
    pie_length = 2 * r * math.sin((angle / 2) * math.pi / 180)
    t.lt(angle / 2)
    t.fd(r)
    t.lt(90 + (angle / 2))
    t.fd(pie_length)
    t.lt(90 + (angle / 2))
    t.fd(r)
    t.lt(180 - angle / 2)

def cake(t, r, n):
    """Draw a cake with given radius and n pies
    """
    angle = 360 / n
    for i in range(n):
        pie(t, r, angle)

    t.pu()
    t.fd(r*2 + 10)
    t.pd()
    

bob = turtle.Turtle()

cake(bob, 60.0, 5)
cake(bob, 60.0, 6)
cake(bob, 60.0, 7)
cake(bob, 60.0, 10)

turtle.mainloop()