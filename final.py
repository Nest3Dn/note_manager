note = {}

note["username"] = input("Введите имя пользователя: ")
note["titles"] = []

for i in range(3):
    title = input(f"Введите заголовок заметки {i + 1}: ")
    note["titles"].append(title)

note["content"] = input(f"Введите описание заметки: ")
note["status"] = input("Введите статус заметки (Например 'Активна', 'Выполнена'): ")
note["created_date"] = input("Введите дату создания заметки в формате дд.мм.гггг: ")
note["issue_date"] = input("Введите дату истечения заметки в формате дд.мм.гггг: ")

print("\nВаши данные:")
for key, value in note.items():
    print(f"{key.capitalize()}: {value}")