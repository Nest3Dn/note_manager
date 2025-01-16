titles = []

while True:
    user_input = input("Введите заголовок: ")
    if user_input == "": #Если пользователь нажимает Enter и ничего не ввводит, цикл останавливается
        break
    elif user_input in titles: #Если пользователь вводит значение, которое уже вводил ранее, указываем на это
        print("Такой заголовок уже есть")
    else:
        titles.append(user_input) #Добавляем в список данные пользователя
