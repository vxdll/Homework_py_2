# Реализуйте алгоритм нахождения(генерации) рандомного(случайного) числа.(Не используя библиотеки связанные с рандомом)
import time

a = int(input("Укажите min значение для диапозона: "))
b = int(input("Укажите max значение для диапозона: "))

diff = b - a
random = int(time.time_ns())
random = random % diff
random = random + a
print(f"Случайное число в диапозоне [{a},{b}] = {random}")




