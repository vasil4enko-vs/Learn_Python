"""5.8. Генераторы списков (List comprehension).

5.8.1. Список из квадратов целых чисел от 0 до N.
"""

N = 6
a = [0] * N

for i in range(N):
    a[i] = i**2

print(a)
