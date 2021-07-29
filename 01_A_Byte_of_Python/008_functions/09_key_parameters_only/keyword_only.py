"""Функции. - Ключевые параметры."""


def total(initial=5, *numbers, extra_number):
    """
    Функция с ошибкой.

    Args:
        extra_number (int, optional): Не указано значение аргумента.
        initial (int, optional): Первый параметр. Defaults to 5.
    """
    count = initial
    for number in numbers:
        count += number
    count += extra_number
    print(count)


total(10, 1, 2, 3, extra_number=50)
total(10, 1, 2, 3)
# Вызовет ошибку, поскольку мы не указали значение аргумента по
# умолчанию для 'extra_number'.
