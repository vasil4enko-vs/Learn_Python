"""Оператор if. - 4. Равные числа."""

"""Задача 4. Пользователь вводит три целых числа. Два из них равны друг
другу. Выведите третье число, не равное остальным. Если среди введенных
чисел не оказалось двух равных друг другу, выведите строку "Ошибка! Нет
равных чисел.".
"""

print('Введите три целых числа. Минимум два из них должны быть равны друг \
другу.')
a = int(input('1. Введите первое число a: '))
b = int(input('2. Введите аторое число b: '))
c = int(input('3. Введите третье число c: '))

if a == b == c:
    print('Верно. a = b = c')
elif a == b:
    print('Верно. a = b')
elif a == c:
    print('Верно. a = c')
elif b == c:
    print('Верно. b = c')
else:
    print('Ошибка! Нет равных чисел.')
