print("Привет! Я бот FitLife — помогу тебе следить за здоровьем.")
user_name = input("Привет! Как тебя зовут? ")

# Я хочу отметить, что на спринте 1, совершенно точно, не проходили while и try/except, но раз уж вы приввели пример, значит надо добавить,
# я знаю для чего это, но при выполнении задания решил, что надо использовать только то что я проходил на спринте. Про комментарии я тоже не парился, я просто не стирал комментарии задания.
while True:
    age = input("Сколько тебе лет (например, 18)? ")
    try:
        user_age = int(age)
        break
    except ValueError:
        print(f"'{age}' — это не число. Попробуй ещё раз.")

while True:
    weight = input("Введи свой вес в кг (например, 55.5 кг.): ")
    try:
        user_weight = float(weight)
        break
    except ValueError:
        print(f"'{weight}' — это не число. Попробуй ещё раз.")

while True:
    height = input("Введи свой рост в метрах (например, 177 см.): ")
    try:
        user_height = float(height)
        break
    except ValueError:
        print(f"'{height}' — это не число. Попробуй ещё раз.")

bmi = user_weight / (user_height**2)
bmi = round(bmi, 1)

water_needed = user_weight * 30

print(f"Отчет для пользователя: {user_name} ({user_age} г.)")
print(f"Твой Индекс массы тела: {bmi}")
print(f"Рекомендуемая норма воды: {round(water_needed / 1000, 1)} л. в день")
print()
print("Расчет окончен. Будьте здоровы!")
