def add_one(some_list):
    str_dig = ""
    for dig in some_list:
        str_dig += str(dig)
    number = int(str_dig) + 1
    final_list = []
    for char in str (number):
        final_list.append(int(char))
    return final_list
assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")
