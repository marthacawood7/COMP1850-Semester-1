# Worksheet 1.5: Rectangle Class

class Rectangle:
    """
    A rectangle, with a width and a height.
    """
    def __init__(self, width, height):
        """
        Creates a Rectangle, given values for width and height.
        """
        # Add code here to check type and value of provided width & height,
        # raising appropriate exceptions if necessary (see README.md)
        self.width = width
        self.height = height

    def area(self):
        area = width * height
        return area

    def perimeter(self):
        perimeter = width + width + height + height

    def is_sqaure(self):
        if width == height:
            return True

        else:
            return False

shape1 = Rectangle(3, 5)
shape2 = Rectangle(4, 4)

print(shape1)
print(shape2)

    # Implement methods is_square(), area() & perimeter() here
    # (See README.md for details of what they should do)
