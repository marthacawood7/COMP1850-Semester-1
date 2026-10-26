# Week 1.5, Session 1: Task 3
import math

class Point:
    """
    A Point in 2D space.
    """

    # Add constructor here

    def__init__(self, x, y):
        self.x = x
        self.y = y 

    # Add distance() method here
    def distance(self):
        return math.hypot(self.x, self.y)

    # Add distance_to() method here
    # (This will need a parameter representing another point)
    def distance_to(p, q):
        return math.hypot(p.distance(), q.distance())




# Finally, add code here to demonstrate use of Point
p = Point(1.5, 2.0)
q = Point(3, 4.5)
print(p.x)
print(p.y)
print(distance_to(p,q))