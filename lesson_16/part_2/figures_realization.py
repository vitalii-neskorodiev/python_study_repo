from lesson_16.part_2.figure import Figure
from lesson_16.part_2.rectangle import Rectangle
from lesson_16.part_2.square import Square
from lesson_16.part_2.triangle import Triangle

square_f: Square = Square(10)

rectangle: Rectangle = Rectangle(10, 5)

triangle: Triangle = Triangle(5, 6, 9, 3)

figures_list: list[Figure] = [square_f, rectangle, triangle]

list_tuple_perimeter_and_square: list[tuple[int, object]] = [(figure.calculate_perimetr(), figure.calculate_square) for
                                                             figure in figures_list]

for item in list_tuple_perimeter_and_square:
    print(item[0], item[1])
