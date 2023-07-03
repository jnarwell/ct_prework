"""
Question 1:
        Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.
            def hello_name(user_name):
"""
def hello_name(user_name):
    print("hello_"+user_name)

hello_name("USERNAME")

"""
Question 2:
        Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
            def first_odds():
"""

def first_odds():
    for number in range(101):
        if number == 99:
            print(number)
        elif number % 2 == 1:
            print(number, end=", ")

first_odds()

"""
Question 3:
        Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.
            def max_num_in_list(a_list):
"""

def max_num_in_list(a_list):
    if 'current_highest_number' not in locals():
        current_highest_number = a_list[0]
    for number in a_list:
        if current_highest_number < number:
            current_highest_number = number

    return current_highest_number

#number_list = [2, 19, 4, 400, 109, 201]
#print (max_num_in_list(number_list))

"""
Question 4:
        Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).
            def is_leap_year(a_year):
"""

def is_leap_year(a_year):
    if a_year % 4 == 0:
        if a_year % 400 == 0:
            return True
        elif a_year % 100 == 0:
            return False
        else:
            return True
    else:
        return False

#print(is_leap_year(1300))

"""
Question 5:
        Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.
            def is_consecutive(a_list):
"""

def is_consecutive(a_list):
    for number in a_list:
        if 'last_number' not in locals():
            last_number = number-1
        if number - 1 == last_number:
            check = True
        else:
            return False
            break
        last_number = number
    if check == True:
        return True

#number_list = [2,3,4]
#print(is_consecutive(number_list))