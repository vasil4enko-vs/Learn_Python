# sourcery skip: for-append-to-extend, for-index-underscore, list-comprehension, use-itertools-product

"""5.6. Вложенные циклы.

5.6.6. Создание двумерного списка и замена всех нулевых элементов на единицы при помощи
вложенных циклов for.
"""

M, N = list(map(int, input("Введите M и N: ").split()))

zeros = []

for i in range(M):  # noqa: B007
    zeros.append([0] * N)  # noqa: PERF401

print(zeros)

for i in range(M):
    for j in range(N):
        zeros[i][j] = 1
print(zeros)
