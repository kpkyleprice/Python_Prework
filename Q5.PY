def is_consecutive(a_list):
    return sorted(a_list) == list(range(min(a_list), max(a_list)+1))
a_list = [1,2,4,5,6,7,8]
print(is_consecutive(a_list))
a_list = [9,10,11,12,13,14]
print(is_consecutive(a_list))