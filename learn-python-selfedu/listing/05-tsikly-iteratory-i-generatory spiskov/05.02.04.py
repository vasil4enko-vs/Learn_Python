"""5.2. Операторы break, continue и else.

Пример без использования оператора break.
"""

d = [1, 5, 3, 6, 0, -4]
fl_find = False
i = 0
while i < len(d) and d[i] % 2 != 0:
    i += 1

fl_find = i != len(d)

print(fl_find)
