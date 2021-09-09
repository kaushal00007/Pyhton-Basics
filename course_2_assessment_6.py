#Write a function, sublist, that takes in a list of numbers as the parameter. In the function, use a while loop to
# return a sublist of the input list. The sublist should contain the same values of the original list up until it
# reaches the number 5 (it should not contain the number 5).
def sublist(list):
    st =[]
    i = 0
    while i < len(list):
        if list[i] == 5:
            break
        st.append(list[i])
        i += 1
    return st

#Write a function called check_nums that takes a list as its parameter, and contains a while loop that only stops once
# the element of the list is the number 7. What is returned is a list of all of the numbers up until it reaches 7.
def check_nums(list):
    temp = []
    i = 0
    while i <len(list):
        if list[i] == 7:
            break
        temp.append(list[i])
        i += 1
    return temp

#Write a function, sublist, that takes in a list of strings as the parameter. In the function,
# use a while loop to return a sublist of the input list. The sublist should contain the same values
# of the original list up until it reaches the string “STOP” (it should not contain the string “STOP”).
def sublist(name):
    temp = []
    i = 0
    while i <len(name):
        if name[i] == 'STOP':
            break
        temp.append(name[i])
        i += 1
    return temp

#Write a function called stop_at_z that iterates through a list of strings. Using a while loop,
# append each string to a new list until the string that appears is “z”. The function should return the new list.
def stop_at_z(name):
    temp = []
    i = 0
    while i <len(name):
        if name[i] == 'z':
            break
        temp.append(name[i])
        i += 1
    return temp
#Below is a for loop that works. Underneath the for loop, rewrite the problem so that it does the same thing,
# but using a while loop instead of a for loop. Assign the accumulated total in the while loop code to the variable sum2.
# Once complete, sum2 should equal sum1.
sum1 = 0

lst = [65, 78, 21, 33]

for x in lst:
    sum1 = sum1 + x

sum2 = 0
i = 0
while i <len(lst):
    sum2 += lst[i]
    i += 1
#Challenge: Write a function called beginning that takes a list as input and contains a while loop that only stops
# once the element of the list is the string ‘bye’. What is returned is a list that contains up to the first 10 strings,
# regardless of where the loop stops. (i.e., if it stops on the 32nd element, the first 10 are returned. If “bye” is
# the 5th element, the first 4 are returned.) If you want to make this even more of a challenge, do this without slicing
def beginning(list):
    i = 0
    New_list = []

    while i < len(list):
        if list[i] == "bye":
            break
        New_list.append(list[i])
        i = i + 1
    part1 = New_list[:10]
    return part1
