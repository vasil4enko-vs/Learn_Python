"""7.1. Что такое функции. Их объявление и вызов.

Пример словаря в Python.
"""


def send_mail():  # noqa: ANN201
    """Функция имитирующая отправку электронных писем."""
    text = "Уважаемый, Сергей Балакирев! \
Я так и не понял, что такое функция. Объясните лучше!"
    print(text)


send_mail()
send_mail()