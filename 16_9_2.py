class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def rectangleArea(self):
        return self.length * self.width

secondRectangle = Rectangle (5,10)
print(secondRectangle.rectangleArea())