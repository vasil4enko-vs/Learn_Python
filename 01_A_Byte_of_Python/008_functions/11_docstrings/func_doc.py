def print_max(x, y):

    """ Выводит максимальное из двух чисел

    Оба значения должны быть целыми числами.

    """

    x = int(x)  # Конвертируем в целые, если возможно
    y = int(y)

    if x > y:
        print(x, 'наибольшее')
    elif x < y:
        print(y, 'наибольшее')
    else:
        print('Числа равны.')


print_max(3, 5)
print(print_max.__doc__)
