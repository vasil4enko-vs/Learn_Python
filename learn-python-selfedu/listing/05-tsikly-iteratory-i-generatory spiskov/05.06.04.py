# sourcery skip: for-append-to-extend, list-comprehension

"""5.6. Вложенные циклы.

5.6.4. Сложение двух списков при помощи вложенных циклов for.
"""

a = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]
b = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]]
c = []

for i, row in enumerate(a):
    r = []  # список для формирования строки, содержащей суммы соответствующих элементов
    for j, x in enumerate(row):
        r.append(x + b[i][j])

    c.append(r)

print(c)
