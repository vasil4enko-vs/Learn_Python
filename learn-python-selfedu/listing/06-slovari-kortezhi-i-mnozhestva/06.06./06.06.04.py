"""6.6. Генераторы множеств и генераторы словарей.

Пример использования генератора множеств
"""

d = [1, 2, "1", "2", -4, 3, 4]

a = {int(x) for x in d}

print(a)
