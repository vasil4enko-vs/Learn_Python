"""7.2. Оператор return в функциях. Функциональное программирование.

Пример словаря в Python.
"""


def even(x):  # noqa: ANN001, ANN201, D103
    return x % 2 == 0


for i in range(1, 20):
    if even(i):
        print(i)
