"""7.2. Оператор return в функциях. Функциональное программирование.

Пример словаря в Python.
"""

PERIMETER = False
if PERIMETER:

    def get_rect(a, b):  # noqa: ANN001, ANN201, D103
        return 2 * (a + b)
else:

    def get_rect(a, b):  # noqa: ANN001, ANN201, D103
        return a * b


print(get_rect(1.5, 3.8))
