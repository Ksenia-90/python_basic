# Задача_2 Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

file_name = "files/lesson_5_dz_2_file.txt"

count_row = 0

file_in = open(file_name, "r")
for index, line in enumerate(file_in):
    count_row += 1
    count_words = len(line.split(" "))
    print(f"words in row № {index+1}: {count_words}")

print(f"row count:{count_row}")
file_in.close()
