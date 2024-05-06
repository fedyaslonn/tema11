'''
Напишите программу с классом Math. При
инициализации атрибутов нет. Реализовать методы addition,
subtraction, multiplication и division. При передаче в методы
двух числовых параметров нужно производить с
параметрами соответствующие действия и печатать ответ.
'''
class Math:
    @staticmethod
    def addition(a, b):
        return f'Сумма чисел {a + b}'

    @staticmethod
    def substraction(a, b):
        return f'Рзаница чисел {a - b}'

    @staticmethod
    def multiplication(a, b):
        return f'Произведение чисел {a * b}'

    @staticmethod
    def division(a, b):
        return f'Деление чисел {a / b}'

print(Math.substraction(10, 5))
print(Math.addition(19, 3))
print(Math.multiplication(11, 5))
print(Math.division(20, 4))