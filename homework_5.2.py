while True:
    first_number = float(input("Введіть перше число: "))
    operator = input("Введіть операцію: ")
    second_number = float(input("Введіть друге число: "))
    if operator == "+":
        result = first_number + second_number
    elif operator == "-":
        result = first_number - second_number
    elif operator == "*":
        result = first_number * second_number
    elif operator == "/":
        result = first_number / second_number
        if second_number != 0:
            result = first_number / second_number
        else:
            result = "Помилка!"
    else:
        result = "Невірно!"
    print("Рузультат буде: ", result)
    user_choice = input("Введіть 'yes' якщо бажаєте продовжити.")
    if user_choice.lower() != "yes":
        print("Роботу завершеною")
        break