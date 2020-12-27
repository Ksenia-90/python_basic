# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, name, speed, color, is_police):
        self._name = name
        self._speed = speed
        self._color = color
        self._is_police = is_police

    def go(self):
        print("Машина поехала.")

    def stop(self):
        print("Машина остановилась.")

    def turn(self, direction):
        print("Машина повернула: " + direction)

    def show_speed(self):
        print(f"Текущая скорость: {self._speed}")

    def get_color(self):
        return self._color

    def get_name(self):
        return self._name

    def get_speed(self):
        return self._speed

    def is_police(self):
        return self._is_police


class TownCar(Car):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color, False)

    def show_speed(self):
        super().show_speed()
        if self._speed > 60:
            print("Превышение скорости")


class SportCar(Car):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color, False)


class WorkCar(Car):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color, False)

    def show_speed(self):
        super().show_speed()
        if self._speed > 40:
            print("Превышение скорости")


class PoliceCar(Car):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color, True)


tc = TownCar("my Car", 100, "Red")
tc.show_speed()
tc.turn("На лево")
tc.go()
tc.stop()
print(f"Имя: {tc.get_name()}")
print(f"Скорость: {tc.get_speed()}")
print(f"Цвет: {tc.get_color()}")
