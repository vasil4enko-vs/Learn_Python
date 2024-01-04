"""5.9. Вложенные циклы и вложенные генераторы списков.

5.9.7. Вложенный генератор списка.
"""


M, N = 3, 4

matrix = [[a for a in range(M)] for b in range(N)]  # noqa: C416

print(matrix)
