# Структура одного сообщения
chat_msg_1 = {
    "text": "Всем приветы в этом чате",
    "sender": "Васисуалий",
    "date": "31-01-22 21:00",
}

chat_msg_2 = {
    "text": "Йо йо, какие дела?",
    "sender": "Мишаня",
    "date": "31-01-22 22:00",
}

print(chat_msg_1["sender"])
print(chat_msg_1["text"])
print(chat_msg_1["date"])

print(f"[Васисуалий]: Всем приветы в этом чате / 31-01-22 21:00")
print("---------------------------------------------------------")

print(f"[{chat_msg_1['sender']}]: {chat_msg_1['text']} / {chat_msg_1['date']}")
print("-" * 50)


def print_message(message):
    print(f"[{message['sender']}]: {message['text']} / {message['date']}")
    print("-" * 50)


print_message(chat_msg_1)
print_message(chat_msg_2)
