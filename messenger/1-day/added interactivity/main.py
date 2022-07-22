from datetime import datetime

# массив с сообщениями
array_message = [
    {
        "text": "первый первый я второй",
        "sender": "Первый отправитель",
        "date": "31-01-22 21:00",
    }
]


# Функция, которая умеет выводить одно сообщение
def print_message(message):
    print(f"[{message['sender']}]: {message['text']} / {message['date']}")
    print("-" * 50)


def add_message(name, txt):
    message = {
        "text": txt,
        "sender": name,
        "date": datetime.now().strftime("%d-%m-%Y %H:%M"),
    }
    array_message.append(message)


# проверка функции add_message
add_message("Второй второй", "Че хотел, второй")

# вывод истории
for i in array_message:
    print_message(i)

# взаимодействие с пользователем
input_valid = ""
name = "Имя не определено"
while input_valid != "!Q":
    print("Напиши текст:")
    input_valid = input()
    if input_valid == "!name":
        print("Напиши новое имя:")
        name = input()
    else:
        add_message(name, input_valid)
        print_message(array_message[-1])
        print()
        print("Для завершения напиши '!Q', Для изменения имени напиши '!name'")

# вывод последнего сообщения
