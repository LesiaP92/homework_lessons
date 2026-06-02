from unittest import result

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