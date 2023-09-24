"""5.2. Операторы break, continue и else.

Пример использования оператора else
"""

S = 0
N = 0
i = -10

while i < N:
    if i == 0:
        break
    S += 1 / i
    i += 1
else:
    print("Сумма вычислена корректно.")

print(S)
