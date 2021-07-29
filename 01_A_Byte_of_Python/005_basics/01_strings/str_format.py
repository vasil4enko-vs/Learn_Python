"""Основы. - Строки. - Метод format."""


age = 26
name = 'Swaroop'

print('Возраст {0} -- {1} лет.'.format(name, age))
print('Почему {0} забавляется с этим Python?'.format(name))

# Примеры использования - Моя дописка - ВВС

"""Плохо:"""

print('Привет, %s!' % name)

"""Хорошо:"""

print('Привет, {name}!'.format(name=name))

"""Ещё лучше:"""

print(f'Привет, {name}! Ты уже взрослый - {age}')
