# ruff: noqa: PLR2004

"""5.4. Примеры работы оператора цикла for. Функция enumerate.

5.4.5. Функция enumerate().
"""

digs = [4, 3, 100, -53, -30, 1, 34, -8]

for i, d in enumerate(digs):
    if 10 <= abs(d) <= 99:
        digs[i] = 0

print(digs)
