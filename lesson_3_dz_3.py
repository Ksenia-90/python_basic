# Задача_3 Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    args = [a, b, c]
    args.remove(min(a, b, c))
    return sum(args)


result = my_func(
    a=int(input("Введите первый аргумент: ")),
    b=int(input("Введите второй аргумент: ")),
    c=int(input("Введите третий аргумент: "))
)
print(result)
