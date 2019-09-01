# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import math

class Triangle:
    def __init__(self, x1, y1, x2, y2, x3, y3):

        self.ab = self.len_side(x1, y1, x2, y2)
        self.bc = self.len_side(x2, y2, x3, y3)
        self.ca = self.len_side(x3, y3, x1, y1)
        self.perimeter = self.calculation_perimeter(self.ab, self.bc, self.ca)
        self.square = self.calculation_square(self.ab, self.bc, self.ca, self.perimeter)
        self.height = self.cacalculation_height(self.ab, self.square)

    def len_side(self, x1, y1, x2, y2):
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def calculation_perimeter(self, ab, bc, ca):
        return ab + bc + ca

    def calculation_square(self, ab, bc, ca, p):
        p = self.perimeter/2
        return math.sqrt(p*(p - ab)*(p - bc)*(p - ca))

    def cacalculation_height(self, a, s):
        return 2*s/a

abc = Triangle(1, 1, 4, 5, 10, -1)
print(abc.ab, abc.bc, abc.ca, abc.perimeter, abc.square, abc.height)


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapeze:
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):



        self.ab = self.len_side(x1, y1, x2, y2)
        self.bc = self.len_side(x2, y2, x3, y3)
        self.cd = self.len_side(x3, y3, x4, y4)
        self.da = self.len_side(x4, y4, x1, y1)

        self.isosceles = self.trapezoid_check(self.ab, self.bc, self.cd, self.da)
        self.height = self.calculation_h(self.ab, self.cd, y1, y2, y3)
        self.perimeter = self.calculation_perimeter(self.ab, self.bc, self.cd, self.da)
        self.square = self.calculation_square(self.ab, self.bc, self.cd, self.da, self.height)

    def len_side(self, x1, y1, x2, y2):
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def calculation_perimeter(self, ab, bc, cd, da):
        return ab + bc + cd + da

    def calculation_square(self, ab, bc, cd, da, h):
        if ab == cd:
            return ((bc + da)/2)*h
        else:
            return ((ab + cd)/2)*h

    def trapezoid_check(self, ab, bc, cd, da):
        if ab == cd or bc == da:
            return True
        else:
            return False


    def calculation_h(self, ab, cd, y1, y2, y3):
        if ab == cd:
            h = abs(y1 - y2)
        else:
            h = abs(y3 - y2)
        return h

tr = Trapeze( 4, 4, 5, 1, 1, 1, 2, 4,)

print(tr.ab, tr.bc, tr.cd, tr.da, tr.perimeter, tr.square, tr.isosceles)