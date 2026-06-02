
list_num = [1, 2, 3, 4, 5, 6]
length = len (list_num)
midd = (length + 1) //2
first_mums = list_num[:midd]
second_nums = list_num[midd:]
result = [first_mums, second_nums]
print(result)