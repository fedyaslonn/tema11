class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def start(self):
        return f'Автомобиль заведён'

    def stop(self):
        return f'Автомобиль заглущён'

    @property
    def car_color(self):
        return f"Цвет машины {self.color}"


    @car_color.setter
    def car_color(self, color):
        self.color = color

    @property
    def car_type(self):
        return f"Тип машины {self.type}"

    @car_type.setter
    def car_type(self, type):
        self.type = type



    @property
    def car_year(self):
        return f"Год машины {self.year}"

    @car_year.setter
    def car_year(self, year):
        self.year = year

    def __str__(self):
        return f'Цвет машины {self.color}, тип машины {self.type}, год машины {self.year}'

car1 = Car('white', 'sportcar', 1963, )
print(car1)
print(car1.start())
print(car1.stop())
car1.car_year = 2010
print(car1)