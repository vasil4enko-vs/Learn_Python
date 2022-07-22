from flask import Flask, request, render_template
from datetime import datetime
import json

app = Flask(__name__)

db_file = "./data/db.json"  # Путь к файлу
json_db = open(db_file, "rb")  # Открываем файл
data = json.load(json_db)  # Загружаем данные из файла
messages_list = data[
    "messages_list"
]  # Берем сообщения из структуры и кладем в переменную


# Функция сохранения сообщений в файл
def save_messages():
    # Создаем структуру
    data = {
        "messages_list": messages_list,
    }
    # Открываем файл на запись
    json_db = open(db_file, "w")
    json.dump(data, json_db)  # Записываем данные в файл


# Функция, которая умеет выводить одно сообщение
def print_message(message):
    print(f"[{message['sender']}]: {message['text']} / {message['date']}")
    print("-" * 50)


# Функция добавления нового сообщения
def add_message(name, txt):
    message = {
        "text": txt,
        "sender": name,
        "date": datetime.now().strftime("%H:%M"),
        # Хочется, чтобы текущая дата подставлялась автоматически
    }
    messages_list.append(message)  # Добавляем новое сообщение в список


# Пройдем по всем элементам списка
# (переменная m - конкретный элемент списка)
# for m in messages_list:
#     print_message(m)

# Главная страница
@app.route("/")
def index_page():
    return "Hello, welcome to Skillbox Chat"


# Раздел со списком сообщений
@app.route("/get_messages")
def get_messages():
    return {"messages": messages_list}


# # Раздел для отправки сообщения
@app.route("/send_message")
def send_message():
    name = request.args["name"]
    text = request.args["text"]
    add_message(name, text)
    save_messages()  # Сохраняем все сообщение в файл
    return "OK"


# Раздел с визуальным интерфейсом
@app.route("/form")
def form():
    return render_template("form.html")


app.run()
