import random

length = random.randint(3, 10) # розмір списку з діапазоном випадкових чисел

big_list = []
for _ in range (length):
    big_list.append(random.randint(1, 10))
    print(big_list)
small_list = [big_list[0], big_list[2], big_list[-2]]
print(small_list)