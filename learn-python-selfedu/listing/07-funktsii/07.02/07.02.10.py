"""7.2. Оператор return в функциях. Функциональное программирование.

Пример словаря в Python.
"""


def get_max2(a, b):  # sourcery skip: min-max-identity  # noqa: ANN001, ANN201, D103
    return a if a > b else b  # noqa: FURB136


def get_max_3(a, b, c):  # noqa: ANN001, ANN201, D103
    return get_max2(a, get_max2(b, c))


x, y, z = 5, 7, 10

print(get_max_3(x, y, z))
