# ruff: noqa: PLR2004

"""5.4. Примеры работы оператора цикла for. Функция enumerate.

5.4.2. Построение "ёлочки"
"""

n = int(input("Введите натуральное число не более 100: "))

if n < 1 or n > 100:
    print("Неверно введено натуральное число.")
else:
    p = 1
    for i in range(1, n + 1):
        p *= i

    print(f"Факториал {n}! = {p}")
