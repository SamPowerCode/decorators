'''
The @staticmethod decorator in Python is used to define a method that belongs to a class but 
does not require access to any instance or class-specific data. Static methods are often used 
for utility functions related to the class but do not need to interact with instance 
variables or class variables.
'''


class MathOperations:
    @staticmethod
    def add(x, y):
        """Add two numbers."""
        return x + y

    @staticmethod
    def multiply(x, y):
        """Multiply two numbers."""
        return x * y

# Example usage:
result_add = MathOperations.add(5, 3)
result_multiply = MathOperations.multiply(4, 6)

print(f"Addition Result: {result_add}")      # Output: Addition Result: 8
print(f"Multiplication Result: {result_multiply}")  # Output: Multiplication Result: 24