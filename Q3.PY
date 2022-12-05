def max_num_in_list(a_list):
    maximum = a_list[1]
    for i in range(len(a_list)):
        if a_list[i] > maximum:
            maximum = a_list[i]
    return maximum
a_list = [5, 72, 106, 19, 100]
print(max_num_in_list(a_list))