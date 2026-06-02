import string


user_text = input("Введіть дві літери через дифіз: ")
start_value = user_text[0]
end_value = user_text[2]                #1 - дефіз
all_values = string.ascii_letters       #рядок з алфавітом
result = ""
start_saving = False
for letter in all_values:
    if letter == start_value:
        start_saving = True
    if start_saving == True:
        result = result + letter
    if letter == end_value:
        start_saving = False
        break
print(result)