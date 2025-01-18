from datetime import datetime

current_date = datetime.now()
formatted = current_date.strftime("%d-%m-%Y")
print("Текущая дата:", formatted)

while True:
    try:
        deadline_str = input("Введите дату дедлайна (в формате день-месяц-год):")
        deadline_date = datetime.strptime(deadline_str,"%d-%m-%Y")

        time_difference = deadline_date - current_date
        days_difference = time_difference.days

        if days_difference < 0:
            print(f"Внимание! Дедлайн истек {abs(days_difference):02d} дней назад.")
        elif days_difference == 0:
            print("Дедлайн сегодня!")
        else:
            print(f"До дедлайна осталось {days_difference:02d} дней")

        break
    except ValueError:
        print("Ошибка! Введите дату в правильном формате! (день-месяц-год).")

