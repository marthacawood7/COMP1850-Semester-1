# Week 1.5, Session 1: Task 3
import math

class Point:
    """
    A Point in 2D space.
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y 

    def distance(self):
        return math.hypot(self.x, self.y)

    def distance_to(self, p):
        return math.hypot(self.x - p.x, self.y - p.y)


# Demonstrate use of Point
p = Point(1.5, 2.0)
q = Point(3, 4.5)

print(p.x)
print(p.y)
print(p.distance())
print(p.distance_to(q))



class Circle:
    """
    A circle in 2D space.
    """

    def __init__(self, radius, centre):
        self.radius = radius
        self.centre = centre 

    def area(self, radius):
        area = (self.radius**2)*math.pi
        return area

    def perimeter(self, radius):
        perimeter = (self.radius*2)*math.pi
        return perimeter