"""07.03. Алгоритм Евклида для нахождения НОД.

Тестирование функции get_nod().
"""


def get_nod(a: int, b: int) -> int | None:
    """Вычисляется НОД для 2-х натуральных чисел по алгоритму Евклида.

    :param a: первое натуральное число
    :param b: второе натуральное число
    :return: НОД для 2-х натуральных чисел
    """  # noqa: RUF002
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a

    return a


res = get_nod(18, 24)
print(res)


def test_get_nod(func: callable) -> str | None:
    """Тестирование функции get_nod.

    Args:
        func (int): тестируемая функция

    Returns:
        str: результат тестирования

    """
    # --- test №1 ---
    a = 28
    b = 35
    c = 7
    res = func(a, b)
    if res == c:
        print("test №1 - OK")
    else:
        print("test №1 - FAIL")

    # --- test №2 ---
    a = 100
    b = 1
    c = 1
    res = func(a, b)
    if res == c:
        print("test №2 - OK")
    else:
        print("test №2 - FAIL")


test_get_nod(get_nod)
