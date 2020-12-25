# Задача_5 Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
from functools import reduce

nums_str = "1 3 4 5 67 8 8 56 556 56 656 556 656"
file_name = "files/lesson_5_dz_5_file.txt"

file = open(file_name, "w+")
file.write(nums_str)
file.seek(0)
sums = reduce((lambda x, y: x + y), map(lambda x: int(x), file.read().rstrip().split(" ")))
file.close()
print(f"sum nums from file:{sums}")
