"""Поток команд. - Оператор break."""

while True:
    s = input('Введите что-нибудь: ')
    if s == 'Выход':
        break
    print('Длина строки', len(s))
print('Завершено.')
