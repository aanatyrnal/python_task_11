# 1 Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен
# извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной
# структуры на реальных данных.

import re

class Date:

    @classmethod
    def my_method(cls, param):
        i = param.replace('-', '')
        return i

    @staticmethod
    def my_meth(param1):
        reg = re.compile(r'((1[0-9])|(2[0-9])|(3[0-1])|(0?[0-9]))-((0?[1-9])|(1[0-2]))-([1-2][0-9][0-9][0-9])')
        if reg.match(param1):
            match = re.match(reg, param1)
        else:
            raise ValueError(f'wrong date: {param1}')
        return match.group()


print(Date.my_method('13-06-2095'))

r = Date()
print(r.my_meth('13-06-2095'))