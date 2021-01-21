class NonPositiveDigitException (ValueError):
    pass


class Square:
    def __init__(self, a):
        if a < 0:
            raise NonPositiveDigitException ('Неправильно указана сторона квадрата')

# Создать класс SquareException.
# Добавить в конструктор класса Square собственное исключение NonPositiveDigitException,
# унаследованное от ValueException,
# которое будет срабатывать каждый раз,
# когда сторона квадрата меньше или равна 0.