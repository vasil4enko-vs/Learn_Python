"""7.2. Оператор return в функциях. Функциональное программирование.

Пример словаря в Python.
"""


def get_rect(a, b):  # type: ignore  # noqa: ANN001, ANN201, D103, PGH003
    return 2 * (a + b)


def get_rect(a, b):  # noqa: ANN001, ANN201, D103, F811
    return a * b


print(get_rect(1.5, 3.8))
