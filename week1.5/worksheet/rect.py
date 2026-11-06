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

        if not isinstance(width, int) or not isinstance(height, int):
            raise TypeError("Width and height must be integers")

        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be greater than 0")

        self.width = width
        self.height = height

    def area(self):
        """Returns the area of the rectangle"""
        shape_area = self.width * self.height
        return shape_area

    def perimeter(self):
        """Returns the permieter of the rectangle"""
        shape_perimeter = self.width + self.width + self.height + self.height
        return shape_perimeter

    def is_square(self):
        """Returns true if the rectangle is a square, and false otherwise"""
        if self.width == self.height:
            return True

        else:
            return False


    

shape1 = Rectangle(3, 5)
shape2 = Rectangle(4, 4)

print("Shape 1 area:", shape1.area())
print("Shape 1 perimeter:", shape1.perimeter())
print("Shape 1 is square:", shape1.is_square())

print("Shape 2 area:", shape2.area())
print("Shape 2 perimeter:", shape2.perimeter())
print("Shape 2 is square:", shape2.is_square())

    # Implement methods is_square(), area() & perimeter() here
    # (See README.md for details of what they should do)
