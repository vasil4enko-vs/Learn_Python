"""4.2. Вложенные условия и множественный выбор. Конструкция if-elif-else.

Выбор пункта меню
"""

item = int(input())

if item == 1:
    print("Выбран курс по Python")
elif item == 2:
    print("Выбран курс по C++")
elif item == 3:
    print("Выбран курс по Java")
elif item == 4:
    print("Выбран курс по JavaScript")
else:
    print("Неверный пункт")
