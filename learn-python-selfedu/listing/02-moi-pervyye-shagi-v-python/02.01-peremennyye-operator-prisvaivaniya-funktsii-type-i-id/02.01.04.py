"""2.1. Переменные, оператор присваивания, функции type и id.

Множественное присваивание.
"""

a, b = 1, 2
print(a, b)

a, b = b, a
print(a, b)

print(id(a), id(b))

print(type(a))
