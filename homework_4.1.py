all_numbers = [1, 0, 3, 2, 0, 4, 0, 5]
zeros = all_numbers.count(0) # метод сканує список, і повертає нулі
for _ in range (zeros):
    all_numbers.remove(0) # метод видаляє 0
for _ in range (zeros):
    all_numbers.append(0) # метод додає 0 в кінець
print(all_numbers)