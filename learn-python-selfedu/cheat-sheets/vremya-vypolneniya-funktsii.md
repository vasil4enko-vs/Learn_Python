Пример измерения времени выполнения функций:

```python
import time


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

    # --- test ---
    a = 2
    b = 10_000_000
    c = 2
    st = time.time()
    res = func(a, b)
    et = time.time()
    dt = et - st
    if res == c and dt < 1:
        print("test №3 - OK")
    else:
        print("test №3 - FAIL")

    print(f"Время выполнения: {dt}")
```
