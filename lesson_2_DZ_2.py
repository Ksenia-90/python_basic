#Задача_2 Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

cout_items = int(input("Введите количество элементов списка:"))
my_list = [i for i in range(cout_items)]
for i in range (cout_items):
    my_list[i] = i
print("befor:")
print(my_list)
print("after:")
for number in range(int(len(my_list)/2)):
    index = number * 2
    buffer = my_list[index]
    my_list[index] = my_list[index + 1]
    my_list[index + 1] = buffer
print(my_list)



