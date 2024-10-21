"""7.2. Оператор return в функциях. Функциональное программирование.

Пример словаря в Python.
"""


def get_sqrt(x):  # noqa: ANN001, ANN201, D103
    # sourcery skip: remove-unreachable-code
    res = None if x < 0 else x**0.5
    return res  # noqa: RET504
    return x


a = get_sqrt(49)

print(a)
