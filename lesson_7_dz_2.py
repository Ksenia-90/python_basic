# Задача_2 Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс)
# этого проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто
# и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные
# числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма
# (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
from abc import abstractmethod


class Clothes:
    def __init__(self, size, growth):
        self.size = size
        self.growth = growth

    @abstractmethod
    def get_consumption(self):
        pass

    @property
    def get_consumption_clothes_state(self):
        return f"Параметры, переданные в класс:" \
               f" {self.size}, {self.growth}"


class Coat(Clothes):
    def __init__(self, size, growth):
        super().__init__(size, growth)

    def get_consumption(self):
        return self.size / 6.5 + 0.5


class Jacket(Clothes):
    def __init__(self, size, growth):
        super().__init__(size, growth)

    def get_consumption(self):
        return self.growth * 2 + 0.3


coat = Coat(40, 20)
jacket = Jacket(5, 9)
print(coat.get_consumption())
print(jacket.get_consumption())
print(coat.get_consumption_clothes_state)
