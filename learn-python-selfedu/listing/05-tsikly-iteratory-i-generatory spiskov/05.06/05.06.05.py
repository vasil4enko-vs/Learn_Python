"""5.6. Вложенные циклы.

5.6.5. Удаление лишних пробелов при помощи вложенных циклов for и while.
"""

t = [
    "- Скажи-ка,  дядя, ведь не даром",
    "Я Python выучил с   каналом",  # noqa: RUF001
    "Балакирев что    раздавал?",
    "Ведь были  ж заданья боевые,",
    "Да, говорят,  еще какие!",
    "Недаром помнит    вся Россия",
    "Как мы рубили   их тогда!",  # noqa: COM812, RUF100
]

for i, line in enumerate(t):
    while line.count("  "):
        line = line.replace("  ", " ")  # noqa: PLW2901

    t[i] = line

print(t)
