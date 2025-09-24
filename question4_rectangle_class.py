
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
