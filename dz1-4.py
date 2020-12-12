#Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
input_str = input("Введите положительное число:")
res=0
i=0
while i < len(input_str):
    item = int(input_str[i])
    if item > res:
        res = item
    i += 1
print(res)

