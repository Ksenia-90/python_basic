# Задача_4 Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники
# (принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

# Задача_5 Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и
# передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.

# Задача_6 Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных
# на уроках по ООП.

class Store:
    def __init__(self):
        self.__catalog = {"001": Printer("hp_laser", "green", 2018, 10),
                          "002": Printer("hp", "red", 2019, 20),
                          "003": Scanner("EPSON_2013", "blue", 2021, 700),
                          "004": Scanner("EPSON", "black", 2020, 400),
                          "005": Xerox("Phaser", "red", 2015, 40)}
        self.__store = {}

    def add_to_store(self, article, count):
        if article not in self.__catalog:
            raise ArticleNotFoundException("Внимание!!! Артикул не найден")

        if not isinstance(count, int) or count <= 0:
            raise ValueError("Считать не действительным")

        if article in self.__store.keys():
            self.__store[article] = self.__store[article] + int(count)
        else:
            self.__store[article] = int(count)

    def extract_from_store(self, article, count):
        if article not in self.__catalog:
            raise ArticleNotFoundException("Внимание!!! Артикул не найден")

        if not isinstance(count, int) or count <= 0:
            raise ValueError("count is not valid")

        if article not in self.__store.keys() or self.__store[article] < int(count):
            raise ExtractException(f"low many article:{article}")

        self.__store[article] = self.__store[article] - int(count)

    def __str__(self):
        return self.__store.__str__()


class OfficeEquipment:

    def __init__(self, name, color, year):
        self.name = name
        self.color = color
        self.year = year

    def __repr__(self):
        return f"{self.name}-{self.color}-{self.year}"


class Printer(OfficeEquipment):
    def __init__(self, name, color, year, print_speed):
        super().__init__(name, color, year)
        self.print_speed = print_speed


class Scanner(OfficeEquipment):
    def __init__(self, name, color, year, resolution):
        super().__init__(name, color, year)
        self.resolution = resolution


class Xerox(OfficeEquipment):
    def __init__(self, name, color, year, copy_speed):
        super().__init__(name, color, year)
        self.copy_speed = copy_speed


class ExtractException(Exception):
    def __init__(self, txt):
        self.txt = txt


class ArticleNotFoundException(Exception):
    def __init__(self, txt):
        self.txt = txt


store = Store()
store.add_to_store("001", 3)
store.add_to_store("002", 7)
store.add_to_store("003", 95)
store.add_to_store("004", 50)
store.add_to_store("004", 30)
store.add_to_store("005", 36)
print(store)
store.extract_from_store("004", 60)
print(store)
