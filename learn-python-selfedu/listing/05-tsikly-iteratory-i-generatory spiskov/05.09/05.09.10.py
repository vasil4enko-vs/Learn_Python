"""5.9. Вложенные циклы и вложенные генераторы списков.

5.9.10. Замена строк на столбцы (выполнение транспонирования).
"""

g = [u**2 for u in [x + 1 for x in range(5)]]

print(g)
