class Rectangle:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def __str__(self):
        return '{}(width={}, height={})'.format(type(self).__name__, self.width, self.height)
    
    def set_width(self, width):
        self.width = width
        if isinstance(self, Square):
            self.height = width
        
    def set_height(self, height):
        self.height = height
        if isinstance(self, Square):
            self.width = height
        
    def get_area(self):
        return self.width * self.height
        
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
    
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5
        
    def get_picture(self):
        shape = ''
        if (self.width > 50) or (self.height > 50):
            return 'Too big for picture.'
        else:
            for _ in range(self.height):
                shape += ('*' * self.width) + '\n'
        return shape
        
    def get_amount_inside(self, other):
        in_width = self.width // other.width
        in_height = self.height // other.height
        return in_width * in_height
    
    
    
class Square(Rectangle):
    
    def __init__(self, side):
        super(Square, self).__init__(side, side)
    
    def __str__(self):
        return '{}(side={})'.format(type(self).__name__, self.width)
    
    def set_side(self, side):
        self.height = side
        self.width = side
    
    def width_height(self):
        return self.width, self.height
