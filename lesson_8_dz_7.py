# Задача_7 Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
# создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class ComplexNumbers:
    def __init__(self, real, im):
        self.real = real
        self.im = im

    def __add__(self, other):
        return ComplexNumbers(self.real + other.real, self.im + other.im)

    def __mul__(self, other):
        return ComplexNumbers(self.real * other.real - self.im * other.im, self.im * other.real + self.real * other.im)

    def __str__(self):
        return f"{self.real} + {self.im}i"


a = ComplexNumbers(5, 5)
b = ComplexNumbers(1, 2)

print(f"Сумма: {a + b} ")
print(f"Произведение: {a * b}")
