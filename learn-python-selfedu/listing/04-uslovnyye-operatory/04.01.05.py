"""4.1. Условный оператор if. Конструкция if-else.

Пример использования оператора if.
"""

a = float(input("a: "))
b = float(input("b: "))

if a < b:
    a, b = b, a

print(a, b)
