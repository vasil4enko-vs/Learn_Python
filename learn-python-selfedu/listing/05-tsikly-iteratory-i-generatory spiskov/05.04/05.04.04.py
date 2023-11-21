# ruff: noqa: PLR2004

"""5.4. Примеры работы оператора цикла for. Функция enumerate.

5.4.4. Замена двузначных чисел нулями.
"""

digs = [4, 3, 100, -53, -30, 1, 34, -8]

for i in range(len(digs)):
    if 10 <= abs(digs[i]) <= 99:
        digs[i] = 0

print(digs)
