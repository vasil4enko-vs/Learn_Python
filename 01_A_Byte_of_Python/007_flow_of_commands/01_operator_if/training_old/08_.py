"""Оператор if. - 8. Время года."""

"""Пользователь вводит строку - название времени года. Если введенная
строка - это "Лето", то выведите строку "Тополиный пух, жара, июль",
если "Зима", то "Снеговик, снежки и горка", если "Осень", то "Пора в
школу!", если "Весна", то "Весенняя капель". В случае, если введенная
строка не равна ни одному из предложенных вариантов, программа должна
выводить строку "Ошибка!".
"""

a = str(input('Введите название времени года: '))

if a == 'Лето':
    print('Тополиный пух, жара, июль')
elif a == 'Зима':
    print('Снеговик, снежки и горка')
elif a == 'Осень':
    print('Пора в школу!')
elif a == 'Весна':
    print('Весенняя капель')
else:
    print('Ошибка!')
