import re
import pandas as pd

simple_string = "Amy is 5 years old, and her sister Mary is 2 years old.Ruth and Peter, their parents, have 3 kids."

pattern = '[A-Z][a-z]*'
names = re.findall(pattern, simple_string)
print (names)
def grades():
    with open ("C:\\Pyhton-course\\Assignment-1\\Assets\\grades.txt", "r") as file:
        grades = file.read()
        w = '([A-Z][a-z]+ [A-Z][a-z]+): B'
        grades = re.findall(w, grades)
        return grades






    # YOUR CODE HERE
myname = grades()
print(myname)