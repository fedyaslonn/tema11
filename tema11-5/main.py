'''
Разработать класс SuperStr, который наследует
функциональность стандартного типа str и содержит два
новых метода:
● метод is_repeatance(s), который принимает некоторую
строку и возвращает True или False в зависимости от того,
может ли текущая строка быть получена целым
количеством повторов строки s. Считать, что пустая
строка не содержит повторов
● метод is_palindrom(), который возвращает True или False в
зависимости от того, является ли строка палиндромом вне
зависимости от регистра. Пустую строку считать
палиндромом.
'''

class SuperStr(str):
    def is_repeatance(self, s):
        n = len(self) // len(s)
        return s * n == self

    def is_palindrome(self):
        if len(self) == 0:
            return True
        if self.lower() == self.lower()[::-1]:
            return True
        return False

a = SuperStr('ababa')
print(a.is_palindrome())
b = SuperStr('nepalindrom')
print(b.is_palindrome())
c = SuperStr('abcabc')
print(c.is_repeatance('abc'))
print(c.is_repeatance('av'))