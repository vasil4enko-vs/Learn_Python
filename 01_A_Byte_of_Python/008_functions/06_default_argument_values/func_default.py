"""Функции. - Значения аргументов по умолчанию."""


def say(message='Сообщение', times=1):
    """
    Вывод на экран строки указанное число раз.

    Args:
        message (str, optional): Текст. Defaults to 'Сообщение'.
        times (int, optional): Количество сообщений. Defaults to 1.
    """
    print(message * times)


say()
say('Привет!')
say('Мир! ', 5)
