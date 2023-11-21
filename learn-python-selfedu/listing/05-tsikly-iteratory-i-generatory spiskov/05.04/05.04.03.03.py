"""5.4. Примеры работы оператора цикла for. Функция enumerate.

5.4.3. Объединение слов
"""

words = ["Python", "дай", "мне", "силы", "пройти", "этот", "курс", "до", "конца"]
s = ""
fl_first = True

for w in words:
    s += ("" if fl_first else " ") + w
    fl_first = False

print(s)
