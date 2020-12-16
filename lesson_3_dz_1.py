# Задача_1 Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
def division(dividend, divider):
    res = dividend / divider
    return res


num_1 = int(input("Введите первое число: "))
num_2 = int(input("Введите следующее число: "))
if num_2 != 0:
    division_res = division(num_1, num_2)
    print(f"result: {division_res}")
else:
    print("Внимание на 0 делить нельзя")
