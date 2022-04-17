# 2 Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве делителя программа
# должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class D_zero:
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def division_zero(self):
        try:
            return self.param1 / self.param2
        except ZeroDivisionError:
            print('Деление на ноль запрещено')
        finally:
            print('Программа завершена')


r = D_zero(4, 2)
print(r.division_zero())
r = D_zero(4, 0)
print(r.division_zero())