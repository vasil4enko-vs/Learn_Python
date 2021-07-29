"""Функции. - Оператор 'return'."""


def maximum(x, y):
    """
    Возвращает большее число.

    Args:
        x (int): Первое число.
        y (int): Второе число

    Returns:
        int, str: Большее число, Числа равны.
    """
    if x > y:
        return x
    elif x == y:
        return 'Числа равны'
    else:
        return y


print(maximum(2, 3))
