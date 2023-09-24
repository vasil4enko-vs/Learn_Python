"""5.2. Операторы break, continue и else.

Пример использования оператора continue.
"""

sum_odd = 0
value = 1

while value != 0:
    value = int(input("Введите целое число: "))
    if value % 2 == 0:
        continue

    sum_odd += value
    print(f"Сумма нечетных чисел равна: {sum_odd}")
