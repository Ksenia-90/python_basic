# Задача_4 Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

def my_func(num, power_factor):
    return num ** power_factor


def my_func_with_pow(num, power_factor):
    return pow(num, power_factor)


def my_func_with_for(num, power_factor):
    acc = 1.0
    for i in range(abs(power_factor)):
        acc = acc / num
    return acc


num_1 = int(input("Введите действительное положительное число: "))
num_2 = int(input("Введите целое отрицательное число: "))
print(my_func(num_1, num_2))
print(my_func_with_pow(num_1, num_2))
print(my_func_with_for(num_1, num_2))
