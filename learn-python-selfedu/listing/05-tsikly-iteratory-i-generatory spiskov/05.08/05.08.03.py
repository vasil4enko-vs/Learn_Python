"""5.8. Генераторы списков (List comprehension).

5.8.3. Генерирование списка состоящего из чисел.
"""

d_inp = input("Целые числа через пробел: ")

a = [int(d) for d in d_inp.split()]

print(a)
