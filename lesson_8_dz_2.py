# Задача_2 Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя программа
# должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class CustomException(Exception):
    def __init__(self, txt):
        self.txt = txt


while True:
    try:
        divisible = int(input("Введите делимое: "))
        divider = int(input("Введите делитель: "))
        if divider == 0:
            raise CustomException("Внимание!!!! на 0 делить нельзя")
        print(f"Результат: {divisible / divider}")
        break
    except CustomException as err:
        print(err)
