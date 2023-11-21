# sourcery skip: simplify-generator, sum-comprehension, while-to-for

"""5.1. Оператор цикла while.

Пример использования оператора while.
"""

N = 1000
s = 0
i = 1

while i <= N:
    s += i
    i += 1

print(s)
