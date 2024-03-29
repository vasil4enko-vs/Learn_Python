"""Установка."""

"""Если у вас уже установлен Python 2.x, нет необходимости его удалять
для того, чтобы установить Python 3.0. Обе версии могут быть установлены
в системе одновременно.
"""

"""Установка в GNU/Linux и BSD"""

"""Если вы используете один из дистрибутивов GNU/Linux, таких как
Ubuntu, Fedora, OpenSUSE, Debian, CentOS или {ваш вариант}, или один из
вариантов BSD, как например, FreeBSD, то скорее всего, в вашей системе
уже установлен Python.

Чтобы проверить, установлен ли Python на вашей машине с BSD или
GNU/Linux, откройте эмулятор терминала (например, konsole или
gnome-terminal) и введите команду python -V, как показано ниже.
"""

"""$ python -V
    Python 3.3.0
"""

"""Примечание: $ - это приглашение командной строки. Оно может выглядеть
по- разному в зависимости от настроек вашей ОС, поэтому я буду
обозначать приглашение просто одним символом $.
"""

"""Если вы видите информацию о версии, как показано выше, значит Python
у вас уже установлен.

Если же вы получаете такое сообщение:
"""

"""$ python -V
    bash: Python: command not found
"""

"""это значит, Python у вас не установлен. Это маловероятно, но всё же
возможно.
"""

"""В этом случае у вас будут два варианта установки Python:

    - Скомпилировать Python из исходных текстов
        (https://www.python.org/downloads/source/) и установить его.
        Инструкция по компиляции есть на указанном веб-сайте.
    - Установить бинарные пакеты, используя пакетный менеджер, входящий
        в комплект поставки вашей ОС, как например, apt-get в
        Ubuntu/Debian и других дистрибутивах, основанных на Debian, yum
        в Fedora, pkg_add во FreeBSD, и т.д. Обратите внимание, что для
        этого потребуется соединение с Интернетом. В противном случае вы
        можете любым другим способом скопировать бинарники на свой
        компьютер и установить оттуда.

"""

"""Установка в Windows"""

"""Посетите страницу http://www.python.org/download/ и загрузите
последнюю версию. Установка производится так же, как и для любых других
программ для Windows.

    Осторожно: Когда вам будет предложено отключить некоторые
    "опциональные" компоненты, не отключайте ни одного! Некоторые из
    этих компонентов могут вам пригодиться, особенно IDLE.

Интересно, что большую часть загрузок производят именно пользователи
Windows. Конечно, это не даёт представления о полной картине, поскольку
у большинства пользователей GNU/Linux Python установлен в системе по
умолчанию.
"""

"""Командная строка DOS"""

"""Для использования Python из командной строки Windows, т.е.
приглашения DOS, необходимо установить должным образом переменную PATH.

Для Windows 2000, XP, 2003 , перейдите в "Панель управления" ->
"Система" -> "Дополнительно" -> "Переменные среды". Нажмите на
переменной с именем PATH в отделе "Системные переменные", после этого
выберите "Редактировать" и допишите;C:\Python33 к концу того, что там
уже есть (проверьте, существует ли такой каталог, так как для более
новых версий Python он будет иметь другое имя). Конечно, укажите
действительное имя каталога.

Для более старых версий Windows добавьте следующую строку в файл
C:\AUTOEXEC.BAT : 'PATH=%PATH%;C:\Python33' (без кавычек) и
перезапустите систему. Для Windows NT используйте файл AUTOEXEC.NT.

Для Windows Vista:

    1. Нажмите кнопку "Пуск" и выберите "Панель управления".
    2. Нажмите "Система", справа вы увидите "Просмотр основных сведений
    о вашем компьютере". Слева - список действий, последним из которых
    будет " Дополнительные параметры системы." Нажмите её. Отобразится
    вкладка "Дополнительно" диалога параметров системы. Нажмите кнопку
    "Переменные среды" справа внизу.
    3. В нижнем поле под названием "Системные переменные" прокрутите до
    Path и нажмите кнопку "Редактировать".
    4. Измените путь, как нужно.
    5. Перезапустите систему. Vista не обновляет системные пути до
    перезагрузки.

Для Windows 7:

    1. Щёлкните правой кнопкой мыши на значке "Компьютер" на рабочем
    столе и выберите "Свойства"; иначе - нажмите кнопку "Пуск" и
    выберите "Панель Управления" -> "Система и безопасность" ->
    "Система". Нажмите "Дополнительные параметры системы" слева, а
    затем выберите вкладку "Дополнительно". Внизу нажмите кнопку
    "Переменные среды" и в отделе "Системные переменные" найдите
    переменную PATH, выберите её и нажмите "Редактировать".
    2. Перейдите к концу строки в поле "Значение переменной" и допишите
    ;C:\Python33.
    3. Если значение переменной было %SystemRoot%\system32;, теперь оно примет
    вид %SystemRoot%\system32;C:\Python33
    4. Нажмите "Ok", и всё. Перезагрузка не требуется.
"""

"""Запуск командной строки Python в Windows"""

"""Если вы должным образом установили значение переменной PATH, теперь
можно запускать интерпретатор из командной строки.

Чтобы открыть терминал в Windows, нажмите кнопку "Пуск" и выберите
"Выполнить". В появившемся диалоговом окне наберите cmd и нажмите Enter.

Затем наберите python и проверьте, нет ли ошибок.
"""

"""Для пользователей Mac OS X"""

"""У пользователей Mac OS X Python уже будет установлен в системе. В
противном случае вы можете открыть терминал, нажав Command+Пробел,
набрав в открывшейся строке поиска Terminal и нажав Enter.

Затем установить Homebrew, выполнив:
"""

"""ruby -e "$(curl -fsSkL raw.github.com/mxcl/hom"""

"""После чего установить Python 3 при помощи:"""

"""brew install python3"""

"""А теперь запустите python3 -V и проверьте, нет ли ошибок."""

"""Резюме"""

"""У пользователей систем GNU/Linux и BSD, вероятнее всего, Python уже
установлен. В противном случае его можно установить, используя пакетный
менеджер, поставляемый с вашим дистрибутивом. Для Windows установка
Python сводится к загрузке установщика и двойному щелчку на нём. С этого
момента мы будем считать, что Python 3 в вашей системе установлен.

Далее мы приступим к написанию нашей первой программы на Python.
"""
