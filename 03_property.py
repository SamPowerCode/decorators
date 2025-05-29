'''
The @property decorator in Python is used to define a method as a property, 
allowing you to access it like an attribute. This is useful when you want 
to control access to an attribute, compute its value dynamically, or validate it.
'''

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        """The radius property."""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Set the radius, ensuring it is non-negative."""
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @property
    def area(self):
        """Calculate the area of the circle."""
        return 3.14159 * (self._radius ** 2)

# Example usage:
circle = Circle(5)
print(f"Radius: {circle.radius}")  # Accessing the radius property
print(f"Area: {circle.area}")      # Accessing the area property

circle.radius = 10                 # Using the setter to change the radius
print(f"New Radius: {circle.radius}")
print(f"New Area: {circle.area}")

# Uncommenting the next line will raise a ValueError
# circle.radius = -3
