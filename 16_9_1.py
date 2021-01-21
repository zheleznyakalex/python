import math

class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def circleArea(self):
        return math.pi * self.radius ** 2


circle_1 = Circle(2,3,4)

print(circle_1.circleArea())

def getCircle(x, y, radius):
    return "Круг({},{},{})".format(x, y, radius)

print(getCircle(2,3,4))