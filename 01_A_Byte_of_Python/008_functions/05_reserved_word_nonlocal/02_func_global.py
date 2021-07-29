"""Функции. - Зарезервированное слово 'nonlocal'."""

x = 1


def func_outer():
    """Для сравнения nonlocal и global."""
    x = 2
    print('x равно', x)

    def func_inner():
        """Глобальное присвоение значения переменной."""
        global x
        x = 5

    func_inner()
    print('Локальное x сменилось на', x)


func_outer()

print('Глобальное x =', x)
