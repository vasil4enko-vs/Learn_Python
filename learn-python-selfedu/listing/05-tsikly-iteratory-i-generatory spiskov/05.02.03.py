"""5.2. Операторы break, continue и else.

Пример использования оператора break.
"""

d = [1, 5, 3, 6, 0, -4]
fl_find = False
i = 0

while i < len(d):
    print(i)
    fl_find = d[i] % 2 == 0
    if fl_find:
        break

    i += 1

print(fl_find)
