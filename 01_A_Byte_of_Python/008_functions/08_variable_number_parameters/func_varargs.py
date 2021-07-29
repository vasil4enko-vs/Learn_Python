"""Функции. - Значения аргументов по умолчанию."""


def total(a=5, *numbers, **phonebook):
    """
    Значения аргументов по умолчанию.

    Args:
        a (int, optional): [description]. Defaults to 5.
        numbers (int, optional): [description].
        phonebook (int, optional): [description].
    """
    print('a:', a)
    # проход по всем элементам кортежа:
    for single_item in numbers:
        print('single_item:', single_item)
    # проход по всем элементам словаря:
    for first_part, second_part in phonebook.items():
        print(f'{first_part}:', second_part)


print(total(10, 1, 2, 3, Jack=1123, John=2231, Inge=1560))
