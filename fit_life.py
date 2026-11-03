print("Привет! Я бот FitLife — помогу тебе следить за здоровьем.")
user_name = input("Привет! Как тебя зовут? ")

# Вы просили вызывать int() сразу от input(), без отдельной
# переменной. Вот я исправил, но мне не понятно, зачем:
# из-за этого в случае ошибки нельзя показать, что именно
# ввёл пользователь.
while True:
    try:
        user_age = int(input("Сколько тебе лет (например, 18)? "))
        break
    except ValueError:
        print("Возраст должен быть числом. Попробуй ещё раз.")

while True:
    try:
        user_weight = float(input("Введи вес в кг (например, 55.5): "))
        break
    except ValueError:
        print("Вес должен быть числом. Попробуй ещё раз.")

while True:
    try:
        user_height = float(input("Введи рост в метрах (например, 1.77): "))
        break
    except ValueError:
        print("Рост должен быть числом. Попробуй ещё раз.")

bmi = user_weight / (user_height**2)
bmi = round(bmi, 1)

water_needed = user_weight * 30

print(f"Отчет для пользователя: {user_name} ({user_age} г.)")
print(f"Твой Индекс массы тела: {bmi}")
print(f"Рекомендуемая норма воды: {round(water_needed / 1000, 1)} л. в день")
print()
print("Расчет окончен. Будьте здоровы!")
