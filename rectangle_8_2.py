from rectangle_8_1 import Rectangle, Square, Circle

rect_1 = Rectangle (3,4)
rect_2 = Rectangle (12,5)

print(rect_1.getArea())
print(rect_2.getArea())

square_1 = Square(5)
square_2 = Square(10)

print(square_1.getAreaSquare(),
      square_2.getAreaSquare())

circle_1 = Circle (17)
circle_2 = Circle (28)

print(circle_1.getAreaCircle(), circle_2.getAreaCircle())

figures = [rect_1, rect_2, square_1, square_2, circle_1, circle_2]

for figure in figures:
    if isinstance(figure,Square):
        print(figure.getAreaSquare())
    elif isinstance(figure,Rectangle):
        print(figure.getArea())
    else:
        print (figure.getAreaCircle ())