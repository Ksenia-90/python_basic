# Задача_1 Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

my_list = []
while True:
    line = input("Введите текст: ")
    if line == '':
        print(my_list)
        break
    newline = line + '\n'
    my_list.append(newline)

file_name = "files/lesson_5_dz_1_file.txt"
with open(file_name, "w") as file_obj:
    file_obj.writelines(my_list)
file_obj.close()
