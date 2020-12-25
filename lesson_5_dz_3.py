# Задача_3 Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

file_name = "files/lesson_5_dz_3_file.txt"
total_salary = 0
row_count = 0
file_in = open(file_name, "r")

for index, line in enumerate(file_in):
    people = line.split(" ")
    total_salary += int(people[1])
    row_count = index + 1
    if int(people[1]) < 20000:
        print(people[0])

print(f"average salary: {total_salary/row_count}")
file_in.close()
