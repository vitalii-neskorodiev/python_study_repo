# Створіть клас геометричної фігури "Ромб". Клас повинен мати наступні атрибути:
#
# сторона_а (довжина сторони a).
# кут_а (кут між сторонами a і b).
# кут_б (суміжний з кутом кут_а).
# Необхідно реалізувати наступні вимоги:
#
# Значення сторони сторона_а повинно бути більше 0.
# Кути кут_а та кут_б повинні задовольняти умову: кут_а + кут_б = 180
# Протилежні кути ромба завжди рівні, тому при заданому значенні кут_а, значення кут_б обчислюється автоматично.
# Для встановлення значень атрибутів використовуйте метод setattr.


class Rhombus:
    def __init__(self, side_a, angle_a):
        setattr(self, 'side_a', side_a)
        setattr(self, 'angle_a', angle_a)
        setattr(self, 'angle_b', 180 - angle_a)

    def set_side_a(self, side_a):
        if side_a > 0:
            setattr(self, 'side_a', side_a)
        else:
            raise ValueError("Значення сторони side_а повинно бути більше 0")

    def set_angle_a(self, angle_a):
        if 0 < angle_a < 180:
            setattr(self, 'angle_a', angle_a)
            setattr(self, 'angle_b', 180 - angle_a)
        else:
            raise ValueError("Кут повинен бути більше 0 і менше 180 градусів")

    def display_info(self):
        print(f"Довжина сторони a: {self.side_a}")
        print(f"Кут між сторонами a і b: {self.angle_a}°")
        print(f"Суміжний кут: {self.angle_b}°")


rhombus = Rhombus(5, 100)
rhombus.display_info()
