"""4.2. Вложенные условия и множественный выбор. Конструкция if-elif-else.

Поиска максимального из трёх чисел
"""

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if a > b:
    if a > c:
        print("a -> max")
    else:
        print("c -> max")
else:
    if b > c:
        print("b -> max")
    else:
        print("c -> max")
