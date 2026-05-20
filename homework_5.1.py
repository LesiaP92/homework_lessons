import string
import keyword
name = input("Ім`я вашої змінної?:")
valid = True
if len (name) == 0:
    valid = False
elif name[0].isdigit():
    valid = False
elif not name.islower() and not name == "_":      #не може містити великі літери
    for char in name:            #перевірка на великі літери з тимчас змінною
        if char.isupper():       # якшо є велика літера то false
            valid = False
if "__" in name:
    valid = False
if name in keyword.kwlist:      # список заборонених слів, перевірка чи є збіг з ним
    valid = False
not_punctuation = string.punctuation.replace("_", "")   #рядок з усіма знаками, змінює _ на нічого
for char in name:
    if char == " ":
        valid = False
    if char in not_punctuation:
        valid = False
print(valid)
