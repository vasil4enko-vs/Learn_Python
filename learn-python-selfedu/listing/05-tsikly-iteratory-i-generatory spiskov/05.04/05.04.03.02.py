# sourcery skip: use-fstring-for-concatenation, use-join

"""5.4. Примеры работы оператора цикла for. Функция enumerate.

5.4.3. Объединение слов
"""

words = ["Python", "дай", "мне", "силы", "пройти", "этот", "курс", "до", "конца"]
s = ""

for w in words:
    s += " " + w

print(s.lstrip())
