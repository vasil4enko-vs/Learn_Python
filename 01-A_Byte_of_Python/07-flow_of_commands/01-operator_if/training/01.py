""" Пользователь вводит два целых числа. Выведите меньшее из них. """

a = int(input('Введите первое целое число: '))
b = int(input('Введите второе целое число: '))

if a < b:
    print('Меньшее число: {0}'.format(a))
elif a > b:
    print('Меньшее число: {0}'.format(b))
else:
    print('Эти числа равны')