# sourcery skip: for-append-to-extend, for-index-underscore, list-comprehension

"""5.6. Вложенные циклы.

5.6.6. Создание двумерного списка при помощи цикла for.
"""

M, N = list(map(int, input("Введите M и N: ").split()))

zeros = []

for i in range(M):  # noqa: B007
    zeros.append([0] * N)  # noqa: PERF401

print(zeros)
