list_numbers = [1, 2, 3, 4, 5]
if len (list_numbers) > 1:
    last_element = list_numbers.pop()
    list_numbers.insert(0, last_element)
print(list_numbers)
