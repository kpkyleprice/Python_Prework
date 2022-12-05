#1
def hello_name(USER_NAME):
    print("hello_"+USER_NAME + "!")
user_name = input('Enter USERNAME: ')
hello_name(user_name)

#2
def first_odd():
    for i in range(1,101):
        if i % 2 != 0:
            print(i)
first_odd()

#3
def max_num_in_list(a_list):
    maximum = a_list[1]
    for i in range(len(a_list)):
        if a_list[i] > maximum:
            maximum = a_list[i]
    return maximum
a_list = [5, 72, 106, 19, 100]
print(max_num_in_list(a_list))

#4
def is_leap_year(a_year):
    if(a_year % 400 == 0):
        return True
    elif a_year % 100 == 0:
        return False
    elif a_year%4 == 0:
        return True
    else:
        return False 
a_year = int(input())
print(is_leap_year(a_year))