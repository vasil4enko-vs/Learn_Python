"""Основы. - Строки. - Метод format."""


age = 26
name = 'Swaroop'

print(f'Возраст {name} -- {age} лет.')
print(f'Почему {name} забавляется с этим Python?')

print('Возраст {0} -- {1} лет.'.format(name, age))
print('Почему {0} забавляется с этим Python?'.format(name))

# Примеры использования - Моя дописка - ВВС

"""Очень плохо:"""

print('Привет, %s!' % name)

"""Плохо:"""

print('Привет, {name}!'.format(name=name))

"""Хорошо:"""

print(f'Привет, {name}! Ты уже взрослый - {age} лет.')
