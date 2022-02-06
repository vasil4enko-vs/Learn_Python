print("Привет всем участникам интенсива")
speaker = "Мишаня"
# duration = 120  # Длительность в минутах
duration = 140  # Длительность в минутах
intensive_name = "Знакомство с Python"
# print - это команда, которая выводит сообщение на экран
print(intensive_name)
# Если перед первой кавычкой ставить f
# то строка станет форматированной
print(f"Сегодня ведущий: {speaker}")

# round -   функция для округления
duration_hours = round(duration / 60)
print(f"Длительность: {duration} минут / {duration_hours} часа")

if duration > 120:
    print("Запасайтесь печеньками.")
    print("Эфир будет длинный.")
else:
    print("Эфир будет короткий. Заварите чайку.")

# len - считает количество символов в строке
print(len(intensive_name))

# Сохраним все данные в одной переменной - словаре
intensive_data = {
    "name": "Знакомство с Python",
    "speaker": "Мишаня",
    "duration": "120"
}


print(intensive_data["name"])
