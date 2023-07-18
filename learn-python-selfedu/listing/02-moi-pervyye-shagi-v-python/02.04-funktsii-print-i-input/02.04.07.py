"""2.4. Функции print и input.

Примеры использования функции input().
Ввод вещественного числа. Функция `float()`.
"""

# print(float("123.45"))

# a = float(input())
# print(a, type(a))
# b = abs(a)
# print(b)

# a = float(input())
# b = float(input())
# print("Периметр:", 2 * (a + b))

# a = float(input("Введите длину прямоугольника: "))
# b = float(input("Введите ширину прямоугольника: "))
# print("Периметр:", 2 * (a + b))

# a, b = map(float, input("Введите две стороны прямоугольника через пробел: ").split())
# print("Периметр:", 2 * (a + b))

# a, b, с = map(int, input("Введите стороны треугольника через пробел: ").split())
# print("Периметр:", a + b + c)

a, b, c = map(int, input("Введите стороны треугольника через пробел: ").split())
print("Периметр:", a + b + c)
