# A bad class implementation

# What does the runtime error mean?
# means that 3 arguments were given, but

# How do we fix the code?
#need to add self into the list of parameters


class Point:
    """
    A point in 2D space.
    """

    def __init__(self, x_coordinate, y_coordinate):
        """
        Creates a Point, given x & y coordinates.
        """
        x = x_coordinate
        y = y_coordinate


p = Point(1.5, 2.0)
print(p.x)
print(p.y)
