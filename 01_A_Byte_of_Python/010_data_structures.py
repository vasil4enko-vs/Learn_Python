"""Структуры данных."""

"""Структуры данных - это, по сути, и есть структуры, которые могут
хранить некоторые данные вместе. Другими словами, они используются для
хранения связанных данных.

В Python существуют четыре встроенных структуры данных: список, кортеж,
словарь и множество. Посмотрим, как ими пользоваться, и как они могут
облегчить нам жизнь.
"""

"""Список"""

"""Список[1] - это структура данных, которая содержит упорядоченный
набор элементов, т.е. хранит последовательность элементов. Это легко
представить, если вспомнить список покупок, в котором перечисляется, что
нужно купить, с тем лишь исключением, что в списке покупок каждый
элемент обычно размещается на отдельной строке, тогда как в Python они
разделяются запятыми.

Список элементов должен быть заключён в квадратные скобки, чтобы Python
понял, что это список. Как только список создан, можно добавлять,
удалять или искать элементы в нём. Поскольку элементы можно добавлять и
удалять, мы говорим, что список - это изменяемый тип данных, т.е. его
можно модифицировать.
"""

"""Краткое введение в объекты и классы"""

"""Хотя я и старался до сих пор оттянуть обсуждение объектов и классов,
на данном этапе всё же необходимо некоторое пояснение, чтобы вы лучше
поняли идею списков. Мы изучим эту тему детально в её собственной главе
- Объектно-ориентированное программирование.

Список - это один из примеров использования объектов и классов. Когда мы
назначаем некоторой переменной i значение, скажем, целое число 5, это
можно представить себе как создание объекта (т.е. экземпляра) i класса
(т.е. типа) int. Чтобы лучше понять это, прочитайте help(int).

Класс может также иметь методы, т.е. функции, определённые для
использования только применительно к данному классу. Этот функционал
будет доступен только когда имеется объект данного класса. Например,
Python предоставляет метод append для класса list, который позволяет
добавлять элемент к концу списка. Так mylist.append('and item') добавит
эту строку к списку mylist. Обратите внимание на обозначение точкой для
доступа к методам объектов.

Класс также может иметь поля, которые представляют собой не что иное,
как переменные, определённые для использования только применительно к
данному классу. Эти переменные/имена можно использовать только тогда,
когда имеется объект этого класса. Доступ к полям также осуществляется
при помощи точки. Например, mylist.field."""

"""Пример: (сохраните как using_list.py)"""

# Это мой список покупок
shoplist = ['яблоки', 'манго', 'морковь', 'бананы']

print('Я должен сделать', len(shoplist), 'покупки.')

print('Покупки:', end=' ')
for item in shoplist:
    print(item, end=' ')

print('\nТакже нужно купить риса.')
shoplist.append('рис')
print('Теперь мой список покупок таков:', shoplist)

print('Отсортирую-ка я свой список')
shoplist.sort()
print('Отсортированный список покупок выглядит так:', shoplist)

print('Первое, что мне нужно купить, это', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('Я купил', olditem)
print('Теперь мой список покупок:', shoplist)

"""Вывод:"""

"""$ python3 using_list.py
    Я должен сделать 4 покупки.

    Покупки: яблоки манго морковь бананы
    Также нужно купить риса.
    Теперь мой список покупок таков: ['яблоки', 'манго', 'морковь',
    'бананы', 'рис']
    Отсортирую-ка я свой список
    Отсортированный список покупок выглядит так: ['бананы', 'манго',
    'морковь', 'рис', 'яблоки']
    Первое, что мне нужно купить, это бананы
    Я купил бананы
    Теперь мой список покупок: ['манго', 'морковь', 'рис', 'яблоки']
    """

"""Как это работает:"""

"""Переменная shoplist - это список покупок человека, идущего на рынок.
В shoplist мы храним только строки с названиями того, что нужно купить,
однако в список можно добавлять любые объекты, включая числа или даже
другие списки.

Мы также использовали цикл for..in для итерации по элементам списка. Вы
уже, наверное, поняли, что список является также и последовательностью.
Особенности последовательностей будут рассмотрены ниже.

Обратите внимание на использование ключевого аргумента end в функции
print, который показывает, что мы хотим закончить вывод пробелом вместо
обычного перевода строки.

Далее мы добавляем элемент к списку при помощи append - метода объекта
списка, который уже обсуждался ранее. Затем мы проверяем, действительно
ли элемент был добавлен к списку, выводя содержимое списка на экран при
помощи простой передачи этого списка функции print, которая аккуратно
его печатает.

Затем мы сортируем список, используя метод sort объекта списка. Имейте в
виду, что этот метод действует на сам список, а не возвращает изменённую
его версию. В этом отличие от того, как происходит работа со строками.
Именно это имеется в виду, когда мы говорим, что списки изменяемы, а
строки - неизменяемы.

Далее после совершения покупки мы хотим удалить её из списка. Это
достигается применением оператора del. Мы указываем, какой элемент
списка мы хотим удалить, и оператор del удаляет его. Мы указываем, что
хотим удалить первый элемент списка, и поэтому пишем "del shoplist[0]"
(помните, что Python начинает отсчёт с 0).

Чтобы узнать более детально обо всех методах объекта списка, просмотрите
help(list).
"""

"""Кортеж"""

"""Кортежи служат для хранения нескольких объектов вместе. Их можно
рассматривать как аналог списков, но без такой обширной
функциональности, которую предоставляет класс списка. Одна из важнейших
особенностей кортежей заключается в том, что они неизменяемы, так же,
как и строки. Т.е. модифицировать кортежи невозможно.

Кортежи обозначаются указанием элементов, разделённых запятыми; по
желанию их можно ещё заключить в круглые скобки.

Кортежи обычно используются в тех случаях, когда оператор или
пользовательская функция должны наверняка знать, что набор значений,
т.е. кортеж значений, не изменится.
"""

"""Пример: (сохраните как using_tuple.py)"""

zoo = ('питон', 'слон', 'пингвин')  # помните, что скобки не обязательны
print('Количество животных в зоопарке -', len(zoo))

new_zoo = 'обезьяна', 'верблюд', zoo
print('Количество клеток в зоопарке -', len(new_zoo))
print('Все животные в новом зоопарке:', new_zoo)
print('Животные, привезённые из старого зоопарка:', new_zoo[2])
print('Последнее животное, привезённое из старого зоопарка -', new_zoo[2][2])
print('Количество животных в новом зоопарке -', len(
    new_zoo) - 1 + len(new_zoo[2]))

"""Вывод:"""

"""$ python3 using_tuple.py
    Количество животных в зоопарке - 3
    Количество клеток в зоопарке - 3
    Все животные в новом зоопарке: ('обезьяна', 'верблюд', ('питон',
    'слон', 'пингвин'))
    Животные, привезённые из старого зоопарка: ('питон', 'слон',
    'пингвин')
    Последнее животное, привезённое из старого зоопарка - пингвин
    Количество животных в новом зоопарке - 5
"""

"""Как это работает:"""

""" Переменная zoo обозначает кортеж элементов. Как мы видим, функция
    len позволяет получить длину кортежа. Это также указывает на то, что
    кортеж является последовательностью.

    Теперь мы перемещаем этих животных в новый зоопарк, поскольку старый
    зоопарк закрывается. Поэтому кортеж new_zoo содержит тех животных,
    которые уже там, наряду с привезёнными из старого зоопарка.
    Возвращаясь к реальности, обратите внимание на то, что кортеж внутри
    кортежа не теряет своей индивидуальности.

    Доступ к элементам кортежа осуществляется указанием позиции
    элемента, заключённой в квадратные скобки - точно так же, как мы это
    делали для списков. Это называется оператором индексирования. Доступ
    к третьему элементу в new_zoo мы получаем, указывая new_zoo[2], а
    доступ к третьему элементу внутри третьего элемента в кортеже
    new_zoo - указывая new_zoo[2][2]. Это достаточно просто, как только
    вы поймёте принцип.
"""

"""Скобки: Хотя скобки и не являются обязательными, я предпочитаю всегда
указывать их, чтобы было очевидно, что это кортеж, особенно в
двусмысленных случаях. Например, print(1,2,3) и print( (1,2,3) ) делают
разные вещи: первое выражение выводит три числа, тогда как второе -
кортеж, содержащий эти три числа.
"""

"""Кортеж, содержащий 0 или 1 элемент: Пустой кортеж создаётся при
помощи пустой пары скобок - "myempty = ()". Однако, с кортежем из одного
элемента не всё так просто. Его нужно указывать при помощи запятой после
первого (и единственного) элемента, чтобы Python мог отличить кортеж от
скобок, окружающих объект в выражении. Таким образом, чтобы получить
кортеж, содержащий элемент 2, вам потребуется указать
"singleton = (2,)".
"""

"""Замечание для программистов на Perl: Список внутри списка не теряет
своей индивидуальности, т.е. списки не развёртываются, как в Perl. Это
же относится к кортежу внутри кортежа, или кортежу внутри списка, или
списку внутри кортежа и т.д. В Python все они рассматриваются как
объекты, хранящиеся внутри другого объекта - только и всего.
"""

"""Словарь"""

"""Словарь - это некий аналог адресной книги, в которой можно найти
адрес или контактную информацию о человеке, зная лишь его имя; т.е.
некоторые ключи (имена) связаны со значениями (информацией). Заметьте,
что ключ должен быть уникальным - вы ведь не сможете получить корректную
информацию, если у вас записаны два человека с полностью одинаковыми
именами.

Обратите также внимание на то, что в словарях в качестве ключей могут
использоваться только неизменяемые объекты (как строки), а в качестве
значений можно использовать как неизменяемые, так и изменяемые объекты.
Точнее говоря, в качестве ключей должны использоваться только простые
объекты.

Пары ключ-значение указываются в словаре следующим образом: "d = {key1 :
value1, key2 : value2 }". Обратите внимание, что ключ и значение
разделяются двоеточием, а пары друг от друга отделяются запятыми, а
затем всё это заключается в фигурные скобки.

Помните, что пары ключ-значение никоим образом не упорядочены в словаре.
Если вам необходим некоторый порядок, вам придётся отдельно
отсортировать словарь перед обращением к нему.

Словари являются экземплярами/объектами класса dict.
"""

"""Пример: (сохраните как using_dict.py)"""