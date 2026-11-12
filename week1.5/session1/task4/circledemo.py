# Week 1.5, Session 1: Task 4

# Add one or more import statements here to give this program
# access to the Point and Circle classes defined in geometry.py

# Write a program here that
#  - Creates a Point object, to represent the centre of a circle
#  - Creates a Circle object, using the Point object and a value for radius
#  - Displays the area of the circle
#  - Displays the perimeter of the circle

from point import Point
from point import Circle



class CircleInfo:
    centre_x = float(input("Enter x value for centre: "))
    centre_y = float(input("Enter y value for centre: "))

    edge_x = float(input("Enter x value for edge: "))
    edge_y = float(input("Enter y value for edge: "))


    centre = Point(centre_x, centre_y)
    edge = Point(edge_x, edge_y)

    radius = centre.distance_to(edge)
    print(f"Radius: {radius}")


    def __init__(self, radius):
        self.radius = radius
        self.area = area(self, radius)
        self.perimeter = perimeter(self, radius)
        return area,perimeter


