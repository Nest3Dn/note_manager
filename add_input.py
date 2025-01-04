username = input("Введите имя пользователя: ")
title = input("Введите заголовок заметки: ")
content = input("Введите описание заметки: ")

content1 = input("Введите первый пункт описания заметки: ")
content2 = input("Введите второй пункт описания заметки: ")
content3 = input("Введите третий пункт описания заметки: ")
contents = [content1, content2, content3]

status = input("Введите статус заметки: ")
created_date = input("Введите дату создания заметки в формате: дд.мм.гггг: ")
issue_date = input("Введите дату истечения заметки в формате: дд.мм.гггг: ")

print("\nВаши данные:")
print("Имя пользователя:", username)
print("Заголовок заметки:", title)
print("Описание заметки", content)
print("Задачи:", contents)
print("Статус заметки:", status)
print("Дата создания заметки:", created_date[:-5:])
print("Дата истечения заметки:", issue_date[:-5:])