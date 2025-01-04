username = input("Введите имя пользователя: ")
title = input("Введите заголовок заметки: ")

titles = []
for i in range(3):
    title = input(f"Введите заголовок заметки {i + 1}: ")
    titles.append(title)

content = input("Введите описание заметки: ")

contents = []
for i in range(3):
    content = input(f"Введите заголовок заметки {i + 1}: ")
    contents.append(content)

status = input("Введите статус заметки: ")
created_date = input("Введите дату создания заметки в формате: дд.мм.гггг: ")
issue_date = input("Введите дату истечения заметки в формате: дд.мм.гггг: ")

print("\nВаши данные:")
print("Имя пользователя:", username)
print("Заголовок заметки:", titles)
print("Описание заметки", content)
print("Задачи:", contents)
print("Статус заметки:", status)
print("Дата создания заметки:", created_date[:-5:])
print("Дата истечения заметки:", issue_date[:-5:])