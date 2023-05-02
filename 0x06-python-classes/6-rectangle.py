class Rectangle:
    """A Rectangle Class"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes the data."""
        self.width(width)
        self.height(height)

        Rectangle.number_of_instances += 1

    def width(self):
        return self.width
    
    def width(self, value):
        if isinstance(value, int) == False:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.width = value

    def height(self):
         return self.height
    
    def height(self, value):
        if isinstance(value, int) == False:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return 2*(self.width + self.height)
        
    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        return "#Rectangle(" + str(self.width) + "," +  str(self.height) +  ")"

    def __repr__(self):
        return "Rectangle(" + str(self.width) + "," +  str(self.height) +  ")"
    



