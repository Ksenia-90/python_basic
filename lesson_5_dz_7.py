# Задача_7 Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджеры контекста.
import json

out = []
firms_dict = {}
file_name_in = "files/lesson_5_dz_7_file_in.txt"
file_name_out = "files/lesson_5_dz_7_file_out.txt"
file_in = open(file_name_in, "r")
good_profit_count = 0
total_profit = 0

for row in file_in:
    item = row.strip().split(" ")
    profit = int(item[2]) - int(item[3])
    if profit > 0:
        good_profit_count += 1
        total_profit += profit
    firms_dict[item[0]] = profit
file_in.close()
avg_dict = {"average_profit": total_profit / good_profit_count}

with open(file_name_out, "w") as file_out:
    json.dump([firms_dict, avg_dict], file_out)
file_out.close()
