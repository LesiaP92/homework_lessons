from unittest import result


def common_elements():
    first_list = []
    for x in range(100):
        if x %3 == 0:
            first_list.append(x)
    second_list = []
    for x in range(100):
        if x % 5 == 0:
            second_list.append(x)
    first_set = set (first_list)
    second_set = set (second_list)
    result_set = first_set.intersection(second_set)
    return result_set
print(common_elements())


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
