# sourcery skip: set-comprehension
"""6.6. Генераторы множеств и генераторы словарей.

Решение задачи 6.6.4 через цикл
"""

d = [1, 2, "1", "2", -4, 3, 4]

set_d = set()
for x in d:
    set_d.add(int(x))

print(set_d)
