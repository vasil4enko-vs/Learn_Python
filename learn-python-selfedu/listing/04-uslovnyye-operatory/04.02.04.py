"""4.2. Вложенные условия и множественный выбор. Конструкция if-elif-else.

Выбор пункта меню
"""

item = int(input())

if item == 1:
    print("Выбран курс по Python")
else:
    if item == 2:
        print("Выбран курс по C++")
    else:
        if item == 3:
            print("Выбран курс по Java")
        else:
            if item == 4:
                print("Выбран курс по JavaScript")
            else:
                print("Неверный пункт")
