#Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

revenue = float(input("Выручка фирмы:"))
costs = float(input("Издержки фирмы:"))
if revenue > costs:
    profitability_of_proceeds = revenue / costs * 100
    print("Прибыль. Рентабельность фирмы:", profitability_of_proceeds, end= '%\n')
    workers = int(input("Количество сотрудников в фирме:"))
    print(f"Прибыль на одного сотрудника : {revenue / workers}")
elif revenue == costs:
    print("NB!!! Фирма сработала в ноль")
else:
    print("NB!!! Фирма работает в убыток")


