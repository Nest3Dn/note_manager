status = "Статус вашей заметки: В процессе"
print(status)

print("""Выберите новый статус заметки:)
1. Выполнено
2. В процессе
3. Отложено
4. Свой вариант""")

while True:
   status_update = (input("Введите новый статус: "))
   if status_update == "1":
      print("Статус вашей заметки обновлен на: Выполнено")
      break
   elif status_update == "2":
      print("Статус вашей заметки обновлен на: В процессе")
      break
   elif status_update == "3":
      print("Статус вашей заметки обновлен на: Отложено")
      break
   elif status_update == "4":
      new_status = input("Введите ваш вариант: ")
      print("Статус вашей заметки обновлен на:", new_status)
      break
   elif status_update == "":
      print("Попробуйте снова")

status = status_update