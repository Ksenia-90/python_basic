# Задача_4 Создать (не программно) текстовый файл со следующим содержимым:
# №One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
translator = {
    "One": "Один",
    "Two": "Два",
    "Three": "Три",
    "Four": "Четыре"
}

file_name_in = "files/lesson_5_dz_4_file_in.txt"
file_name_out = "files/lesson_5_dz_4_file_out.txt"

file_in = open(file_name_in, "r")
file_out = open(file_name_out, "w")

for row in file_in:
    worlds = row.rstrip().split(" ")
    worlds[0] = translator.get(worlds[0])
    print(" ".join(worlds), file=file_out)

file_out.close()
file_in.close()
