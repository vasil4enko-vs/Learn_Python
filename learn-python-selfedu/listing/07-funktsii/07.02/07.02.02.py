"""7.2. Оператор return в функциях. Функциональное программирование.

Пример словаря в Python.
"""


def send_mail(from_name, old):  # noqa: ANN001, ANN201
    """Функция имитирующая отправку электронных писем."""
    text = f"""Уважаемый, Сергей Балакирев!
    Я так и не понял, что такое функция.
    Объясните лучше!
    Ваш, навсегда {from_name}! И не судите меня строго, мне всего {old} лет!"""

    print(text)


def get_sqrt(x):  # noqa: ANN001, ANN201, D103
    res = None if x < 0 else x**0.5
    return res  # noqa: RET504


a = get_sqrt(49)

print(a)