"""Функции. - Ключевые аргументы."""


def func(a, b=5, c=10):
    """
    Функция с параметрами по-умолчанию.

    Args:
        a (int, optional): Первый параметр
        b (int, optional): Второй параметр. Defaults to 5.
        c (int, optional): Третий параметр. Defaults to 10.
    """
    print('a =', a, 'b =', b, 'c = ', c)


func(3, 7)
func(25, c=24)
func(c=50, a=100)
