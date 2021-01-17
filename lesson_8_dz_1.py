# Задача_1 Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать
# число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить
# валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных
# данных.

class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        cls.today = {}
        return sum(map(lambda x: int(x), day_month_year.split("-")))

    @staticmethod
    def validate(day, month, year):
        if 1 <= day <= 31:
            if 2021 >= year >= 0:
                if 1 <= month <= 12:
                    return f"Верно"
                else:
                    return f"Неверно указан год"
            else:
                return f"Неверно указан месяц"
        else:
            return f"Неверно указан день"

    def __str__(self):
        return f"Число {Data.extract(self.day_month_year)}"


data_today = Data("14 - 1 - 2021")
print(data_today)
print(data_today.extract("19 - 6 - 2021"))
print(Data.extract("19 - 6 - 2015"))
print(Data.validate(1, 12, 2005))
print(Data.validate(31, 12, 2025))
print(data_today.validate(19, 19, 1990))
print(data_today.extract("29-22-30"))
