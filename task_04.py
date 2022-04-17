# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные типы
# оргтехники (принтер, сканер, ксерокс). В базовом классе определите параметры, общие для приведённых типов.
# В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.

class Warehouse:
    pass

class Office_equipment:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

class Printer(Office_equipment):
    def print(self):
        print('Печать текста')

class Scanner(Office_equipment):
    def scan(self):
        print('Сделать скан')

class Copier(Office_equipment):
    def copy(self):
        print('Сделать копию')

printer = Printer('Черный', 'Lenovo')
printer.print()

scanner = Scanner('Черный', 'Lenovo')
scanner.scan()