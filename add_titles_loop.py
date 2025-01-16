titles = []

while True:
    user_input = input("Введите заголовок: ")
    if user_input == "":
        break
    elif user_input in titles:
        print("Такой заголовок уже есть")
    else:
        titles.append(user_input)
