"""4.2. Вложенные условия и множественный выбор. Конструкция if-elif-else.

Пример использования вложенного условного оператора.
"""

x = int(input())
MAX_FOR_DIGIT = 9

if x % 2 == 0:
    if 0 <= x <= MAX_FOR_DIGIT:
        print("x - цифра")
    else:
        print("x - число")
