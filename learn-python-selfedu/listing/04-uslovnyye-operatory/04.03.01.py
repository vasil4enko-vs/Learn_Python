"""4.3. Тернарный условный оператор. Вложенное тернарное условие.

Вложенный тернарный оператор.
"""

a = 2
b = 3
c = -4

d = (a if a > c else c) if a > b else (b if b > c else c)
print(d)
