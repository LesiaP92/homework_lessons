number_text = input("Ціле число: ")
start_number = number_text
value = int(start_number)
while value > 9:
    product = 1     #змінна для накопичення добутку цифр
    for char in start_number: #перебирає кожну цифру
        number = int(char)
        product = product * number
    value = product
    start_number = str(product)
print(value)
