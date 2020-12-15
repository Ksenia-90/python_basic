# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента —
# номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры: [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# # (2, {“назвние”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например
# название, а значение — список значений-характеристик, например список названий товаров.
# Пример: {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]

end_input = True
baze = []
index = 1
title_name = "Название"
Price_1 = "Цена"
Count_1 = "Колличество"
units_1 = "Ед."
while end_input:
    name = input("Введите название: ")
    price = float(input("Цена: "))
    count = int(input("Количество: "))
    ed = input("Единицы измерения: ")
    my_dict = {
        title_name: name,
        Price_1: price,
        Count_1: count,
        units_1: ed
    }
    baze.append((index, my_dict))
    exit_ok = True
    while exit_ok:
        retry = input("Продолжить? Д/Н ")
        if retry == "Д":
            exit_ok = False
        elif retry == "Н":
            exit_ok = False
            end_input = False
    index = index + 1
print(baze)
list_names = []
list_prices = []
list_counts = []
list_ed = []
for item in baze:
    list_names.append(item[1].get(title_name))
    list_prices.append(item[1].get(Price_1))
    list_counts.append(item[1].get(Count_1))
    list_ed.append(item[1].get(units_1))
res = {
    title_name: list_names,
    Price_1: list_prices,
    Count_1: list_counts,
    units_1: list_ed
}
print(res)