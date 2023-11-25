"""5.8. Генераторы списков (List comprehension).

5.8.4. Генерирование списка состоящего из строк.
"""

d_inp = input("Целые числа через пробел: ")

a = [d for d in d_inp.split()]  # noqa: C416

print(a)
