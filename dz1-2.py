
#2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

input_sec = int(input("Введите время в секундах:"))
time_hours = input_sec // (60 * 60)
time_minutes = (input_sec % (60 * 60)) // 60
input_sec = (input_sec % (60 * 60)) % 60
text = f'Сейчас: {time_hours:0{2}}:{time_minutes:0{2}}:{input_sec:0{2}}'
print(text)


