# ruff: noqa: PLR2004

"""5.1. Оператор цикла while.

Пример использования оператора while.
"""

N = 1000
s = 0
i = 1

while i <= N and i <= 50:
    s += i
    i += 1

print(s)
