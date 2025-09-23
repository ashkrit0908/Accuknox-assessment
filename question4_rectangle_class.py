
class Rectangle:
    """
    A Rectangle class that can be iterated over.
    """
    
    def __init__(self, length: int, width: int):
        """
        Initialize Rectangle with length and width.
        
        Args:
            length (int): The length of the rectangle
            width (int): The width of the rectangle
            
        Raises:
            TypeError: If length or width are not integers
        """
        if not isinstance(length, int):
            raise TypeError("length must be an integer")
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
            
        self.length = length
        self.width = width
    
    def __iter__(self):
        """
        Make the Rectangle instance iterable.
        
        Returns:
            Iterator: Yields length dict first, then width dict
        """
        # First yield the length
        yield {'length': self.length}
        # Then yield the width
        yield {'width': self.width}
    
    def __repr__(self):
        """String representation of the Rectangle"""
        return f"Rectangle(length={self.length}, width={self.width})"
    
    def area(self):
        """Calculate the area of the rectangle"""
        return self.length * self.width
    
    def perimeter(self):
        """Calculate the perimeter of the rectangle"""
        return 2 * (self.length + self.width)


def test_rectangle_class():
    """Test the Rectangle class functionality"""
    print("=" * 60)
    print("RECTANGLE CLASS TEST")
    print("=" * 60)
    
    # Test 1: Basic initialization
    print("Test 1: Basic initialization")
    rect = Rectangle(10, 5)
    print(f"Created: {rect}")
    print(f"Area: {rect.area()}")
    print(f"Perimeter: {rect.perimeter()}")
    
    # Test 2: Iteration
    print("\nTest 2: Iteration")
    print("Iterating over rectangle:")
    for item in rect:
        print(f"  {item}")
    
    # Test 3: Multiple iterations
    print("\nTest 3: Multiple iterations")
    print("First iteration:")
    for item in rect:
        print(f"  {item}")
    
    print("Second iteration:")
    for item in rect:
        print(f"  {item}")
    
    # Test 4: Unpacking
    print("\nTest 4: Unpacking")
    length_dict, width_dict = rect
    print(f"Length dict: {length_dict}")
    print(f"Width dict: {width_dict}")
    
    # Test 5: Type validation
    print("\nTest 5: Type validation")
    try:
        bad_rect = Rectangle("10", 5)
    except TypeError as e:
        print(f"Caught expected error: {e}")
    
    try:
        bad_rect = Rectangle(10, "5")
    except TypeError as e:
        print(f"Caught expected error: {e}")
    
    # Test 6: Different values
    print("\nTest 6: Different values")
    rect2 = Rectangle(15, 8)
    print(f"Created: {rect2}")
    print("Iterating:")
    for item in rect2:
        print(f"  {item}")

if __name__ == "__main__":
    print("CUSTOM CLASSES - RECTANGLE CLASS TEST")
    print("Testing Rectangle class with iteration requirements")
    print()
    
    test_rectangle_class()
    
    print("\n" + "=" * 60)
    print("Test completed!")
    print("=" * 60)
