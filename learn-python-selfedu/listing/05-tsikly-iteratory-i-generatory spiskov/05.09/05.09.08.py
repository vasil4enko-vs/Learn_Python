"""5.9. Вложенные циклы и вложенные генераторы списков.

5.9.8. Возведение двумерного списка в квадрат.
"""


A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

A = [[x**2 for x in row] for row in A]

print(A)
