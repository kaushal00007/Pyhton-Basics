#Write a function called int_return that takes an integer as input and returns the same integer.
def int_return(num):
    return num

#Write a function called add that takes any number as its input and returns that sum with 2 added.
def add(num):
    return num+2
#Write a function called change that takes any string, adds “Nice to meet you!” to the end of the argument given,
# and returns that new string.
def change(msg):
    return msg + "Nice to meet you!"

#Write a function, accum, that takes a list of integers as input and returns the sum of those integers.
def accum(list):
    sum = 0;
    for l in list:
        sum += l
    return sum
#Write a function, length, that takes in a list as the input. If the length of the list is greater than or equal to 5,
# return “Longer than 5”. If the length is less than 5, return “Less than 5”.
def length(list):
    count = 0
    for l in list:
        count += 1
    if count >= 5:
        return  "Longer than 5"
    else:
        return "Less than 5"
#You will need to write two functions for this problem. The first function, divide that takes in any number and
# returns that same number divided by 2. The second function called sum should take any number, divide it by 2,
# and add 6. It should return this new number. You should call the divide function within the sum function.
# Do not worry about decimals.
def divide(num):
    return num/2
def sum(num1):
    temp = divide(num1)
    return temp + 6