"""Функции. - Зарезервированное слово 'nonlocal'."""

x = 1


def func_outer():
    """Объяснение как сохранить глобальную переменную."""
    x = 2
    print('x равно', x)

    def func_inner():
        """Не локальное присвоение значения переменной."""
        nonlocal x
        x = 5

    func_inner()
    print('Локальное x сменилось на', x)


func_outer()

print('Глобальное x =', x)
