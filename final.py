note = {}

note["username"] = input("Введите имя пользователя: ")
note["titles"] = []

for i in range(3):
    title = input(f"Введите заголовок заметки {i + 1}: ")
    note["titles"].append(title)

note["contents"] = []

for i in range(3):
    content = input(f"Введите описание заметки {i + 1}: ")

note["status"] = input("Введите статус заметки: ")
note["created_date"] = input("Введите дату создания заметки в формате дд.мм.гггг: ")
note["issue_date"] = input("Введите дату истечения заметки в формате дд.мм.гггг: ")

print("\nВаши данные:")
for key, value in note.items():
    print(f"{key.capitalize()}: {value}")
