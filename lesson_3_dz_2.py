# Задача_2 Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия,
# год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def options(name, surname, year, city, email, telephone):
    result = f'{surname}, {name}, {year} год(а), г. {city}, {email}, {telephone}'
    return result


print(options(
    name=input("Введите ваше имя: "),
    surname=input("Введите вашу фамилию: "),
    year=int(input("Ведите год рождения: ")),
    city=input("Введите город проживания: "),
    email=input("Введите ваш email: "),
    telephone=input("Введите ваш телефон: ")
))
