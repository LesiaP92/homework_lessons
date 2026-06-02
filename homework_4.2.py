

lst = [4, 3, 2, 7, 6, 9]
if not lst:
    print (0)
else:
    sum_num = 0
    for i in lst [::2]:
        sum_num = sum_num + i
    result = sum_num * lst [-1]
    print(result)