"""5.9. Вложенные циклы и вложенные генераторы списков.

5.9.9. Замена строк на столбцы (выполнение транспонирования).
"""

A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

A = [[row[i] for row in A] for i in range(len(A[0]))]

print(A)