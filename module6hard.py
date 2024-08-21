import math


class Figure:
    sides_count = 0

    def __init__(self, color: tuple, sides: int, filled=bool):
        self.__sides = [sides for x in range(self.sides_count)]
        self.__color = list(color)
        self.filled = filled

    def __len__(self) -> int:
        return sum(self.__sides)

    def get_color(self) -> list:
        return self.__color

    def __is_valid_color(self, r, g, b) -> bool:
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True
        return False

    def set_color(self, r, g, b) -> list:
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
            return self.__color

    def __is_valid_sides(self, *new_sides) -> bool:
        if len(new_sides) == self.sides_count and all(isinstance(item, int) for item in new_sides):
            return True
        return False

    def get_sides(self) -> list:
        return self.__sides

    def set_sides(self, *new_sides) -> list:
        if self.__is_valid_sides(new_sides):
            self.__sides = list(new_sides)
            return self.__sides


class Circle(Figure):
    sides_count = 1

    def __init__(self, color: tuple, sides: int, filled=bool):
        super().__init__(sides=sides, color=color, filled=filled)
        self.__radius = sides / 2 * math.pi

    def get_square(self) -> float:
        square = math.pi * self.__radius ** 2
        return square


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color: tuple, sides: tuple, filled=bool):
        super().__init__(sides=sides, color=color, filled=filled)
        self.__sides = sides
        self.semiperimeter = sum(self.__sides) / 2
        self.a = self.__sides[0]
        self.b = self.__sides[1]
        self.c = self.__sides[2]

    def get_square(self) -> float:
        squar = (self.semiperimeter * (self.semiperimeter - self.a) * (self.semiperimeter - self.b) * (
                self.semiperimeter - self.c)) ** 0.5
        return squar


class Cube(Figure):
    sides_count = 12

    def __init__(self, color: tuple, sides: int, filled=bool):
        super().__init__(sides=sides, color=color, filled=filled)
        self.__sides = sides

    def get_volume(self) -> int:
        return self.__sides ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
#
# # Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())
#
# # Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
