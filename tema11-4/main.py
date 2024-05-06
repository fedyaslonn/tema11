'''
Программа с классом Sphere для представления сферы
в трёхмерном пространстве. Реализовать методы:
● конструктор, принимающий 4 числа: радиус и координаты
центра сферы x, y, z. Если конструктор вызывается без
аргументов, создать объект сферы с единичным радиусом
и центром в начале координат. Если конструктор
вызывается только с радиусом, создать объект с
соответствующим радиусом и центром в начале
координат
● метод get_volume(), возвращающий число – объем шара,
ограниченного текущей сферой
метод get_square(), возвращающий число – площадь
внешней поверхности сферы
● метод get_radius(), возвращающий число – радиус текущей
сферы
● метод get_center(), возвращающий кортеж с координатами
центра сферы
● метод set_radius(radius), который принимает новое
значение радиуса, меняет радиус текущей сферы и ничего
не возвращает
метод set_center(x, y, z), который принимает новые
значения для координат центра радиуса, меняет
координаты текущей сферы и ничего не возвращает
● метод is_point_inside(x, y, z), который принимает
координаты некой точки в трёхмерном пространстве и
возвращает True или False в зависимости от того,
находится ли точка внутри сферы
'''
import math

class Sphere:
    def __init__(self, radius=1, x=0, y=0, z=0):
        self.x = x
        self.radius = radius
        self.y = y
        self.z = z

    def get_volume(self):
        return (4/3) * math.pi * self.radius ** 3

    def get_square(self):
        return 4 * math.pi * self.radius ** 2

    def get_radius(self):
        return self.radius

    def get_center(self):
        return [self.x, self.y, self.z]

    def set_radius(self, radius):
        self.radius = radius

    def set_center(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def is_point_inside(self, x1, y1, z1):
        return self.x > x1 and self.y > y1 and self.z > z1

    def __str__(self):
        return f'{self.radius, self.x, self.y, self.z}'


sphere = Sphere()
print(sphere)
sphere1 = Sphere(5, 1, 1, 2)
print(sphere1.get_square())
print(sphere1.get_volume())
print(sphere1.get_center())
sphere1.set_radius(3)
print(sphere1)
print(sphere1.is_point_inside(0,0,1))