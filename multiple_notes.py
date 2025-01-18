from datetime import datetime

print("Добро пожаловать в Менеджер заметок! Вы можете добавить новую заметку.")

def create_note():
  name = input("Введите имя пользователя: ")
  title = input("Введите заголовок заметки: ")
  content = input("Введите описание заметки: ")
  status = input("Введите статус заметки: ")

  while True:
      create_date = input("Введите дату создания заметки в формате (день-месяц-год): ")
      try:
          create_date = datetime.strptime(create_date,"%d-%m-%Y")
          formatted1 = create_date.strftime("%d-%m-%Y")
          break
      except ValueError:
          print("Произошла ошибка! Пожалуйста, введите дату в формате (день-месяц-год.")

  while True:
      issue_date = input("Введите дедлайн заметки в формате (день-месяц-год): ")
      try:
        deadline = datetime.strptime(issue_date,"%d-%m-%Y")
        formatted2 = deadline.strftime("%d-%m-%Y")
        break
      except ValueError:
         print("Произошла ошибка! Пожалуйста, введите дату в формате (день-месяц-год).")

  return {
      "Имя": name,
      "Заголовок": title,
      "Описание": content,
      "Статус": status,
      "Дата создания": formatted1,
      "Дедлайн": formatted2
  }

def my_notes(notes):
  if not notes:
      print("Нет сохраненных заметок.")
      return

  for i, note in enumerate(notes):
    print(f"Заметка #{i + 1}")
    for key, value in note.items():
      print(f"  {key}: {value}")

def main():
  notes = []
  while True:
    command = input("Введите 'создать' для добавления заметки или 'стоп' для завершения: ").lower()

    if command == "создать":
      new_note = create_note()
      notes.append(new_note)
      print("Заметка добавлена.")
    elif command == "стоп":
      break
    else:
       print("Неверная команда, попробуйте еще раз.")

  my_notes(notes)

if __name__ == "__main__":
  main()